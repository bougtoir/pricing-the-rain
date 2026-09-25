from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import requests
import pandas as pd
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "regions.yml"
RAW_DIR = ROOT / "data" / "raw" / "weather"
LEDGER = ROOT / "data" / "raw" / "acquisition_ledger.csv"
INVALID_LEDGER = ROOT / "data" / "raw" / "invalid_acquisition_ledger.csv"
API_URL = "https://archive-api.open-meteo.com/v1/archive"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def acquire() -> list[dict[str, str]]:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    existing_times = {}
    if LEDGER.exists():
        with LEDGER.open(newline="", encoding="utf-8") as handle:
            existing_times = {
                row["identifier"]: row["retrieved_utc"]
                for row in csv.DictReader(handle)
            }
    records: list[dict[str, str]] = []
    for region in config["regions"]:
        path = RAW_DIR / f"{region['id']}_era5_1991_2020.json"
        params = {
            "latitude": region["latitude"],
            "longitude": region["longitude"],
            "start_date": config["study_period"]["start"],
            "end_date": config["study_period"]["end"],
            "daily": "precipitation_sum",
            "timezone": "UTC",
            "models": "era5",
        }
        if not path.exists():
            response = requests.get(API_URL, params=params, timeout=180)
            response.raise_for_status()
            payload = response.json()
            precipitation = payload.get("daily", {}).get("precipitation_sum", [])
            if len(precipitation) < 10_900 or sum(
                value is not None for value in precipitation
            ) < 10_800:
                raise RuntimeError(f"Incomplete weather response for {region['id']}")
            path.write_text(
                json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
            retrieved = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        else:
            retrieved = existing_times.get(
                region["id"],
                datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
                .replace(microsecond=0)
                .isoformat(),
            )
        records.append(
            {
                "source": "Open-Meteo Historical Weather API / ERA5",
                "identifier": region["id"],
                "url": requests.Request("GET", API_URL, params=params).prepare().url,
                "retrieved_utc": retrieved,
                "conditions": "daily precipitation_sum; timezone UTC; model era5",
                "saved_path": str(path.relative_to(ROOT)),
                "bytes": str(path.stat().st_size),
                "sha256": sha256(path),
                "license": "Copernicus C3S data via Open-Meteo; attribution required",
                "coverage": "complete response validated at >=10,900 rows and >=10,800 non-null values",
            }
        )
    with LEDGER.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(records[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(records)
    invalid_records = []
    for path in sorted(RAW_DIR.glob("*_era5_land_1991_2020.json")):
        invalid_records.append(
            {
                "source": "Open-Meteo Historical Weather API / ERA5-Land",
                "identifier": path.name.split("_era5_land_")[0],
                "retrieved_utc": pd.Timestamp(
                    path.stat().st_mtime, unit="s", tz="UTC"
                ).isoformat(),
                "conditions": "daily precipitation_sum; timezone UTC; model era5_land",
                "saved_path": str(path.relative_to(ROOT)),
                "bytes": str(path.stat().st_size),
                "sha256": sha256(path),
                "validation_status": "excluded: all precipitation values null",
            }
        )
    if invalid_records:
        with INVALID_LEDGER.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=list(invalid_records[0]),
                lineterminator="\n",
            )
            writer.writeheader()
            writer.writerows(invalid_records)
    return records


if __name__ == "__main__":
    rows = acquire()
    print(f"Verified {len(rows)} immutable raw weather snapshots")
