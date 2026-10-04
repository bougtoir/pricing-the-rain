from __future__ import annotations

import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests
import yaml


ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "config" / "references.yml"
RAW = ROOT / "data" / "raw" / "literature"
LEDGER = ROOT / "data" / "raw" / "literature_acquisition_ledger.csv"
METADATA = ROOT / "analysis" / "reference_metadata.csv"
MANUAL_LEDGER = ROOT / "data" / "raw" / "literature_source_ledger.csv"
AKONGA_LANDING_URL = (
    "https://repository.kulib.kyoto-u.ac.jp/bitstream/"
    "2433/68028/1/ASM_8_71.pdf"
)
AKONGA_PDF_URL = (
    "https://repository.kulib.kyoto-u.ac.jp/server/api/core/bitstreams/"
    "bce8f97f-1a89-4a2f-b261-c3845aebb38e/content"
)


def checksum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slug(doi: str) -> str:
    return doi.lower().replace("/", "_").replace(".", "-")


def acquire() -> None:
    references = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))["references"]
    RAW.mkdir(parents=True, exist_ok=True)
    METADATA.parent.mkdir(parents=True, exist_ok=True)
    existing_times = {}
    if LEDGER.exists():
        with LEDGER.open(newline="", encoding="utf-8") as handle:
            existing_times = {
                row["doi"]: row["retrieved_utc"] for row in csv.DictReader(handle)
            }
    records = []
    metadata_rows = []
    for reference in references:
        doi = reference["doi"]
        path = RAW / f"crossref_{slug(doi)}.json"
        url = f"https://api.crossref.org/works/{quote(doi, safe='')}"
        status = "verified"
        if not path.exists():
            response = requests.get(
                url,
                headers={"User-Agent": "pricing-the-rain/1.0 (mailto:bougtoir@gmail.com)"},
                timeout=120,
            )
            if response.status_code != 200:
                status = f"unavailable: HTTP {response.status_code}"
            else:
                path.write_text(
                    json.dumps(
                        response.json(), ensure_ascii=False, separators=(",", ":")
                    ),
                    encoding="utf-8",
                )
        if path.exists():
            payload = json.loads(path.read_text(encoding="utf-8"))["message"]
            title = (payload.get("title") or [""])[0]
            container = (payload.get("container-title") or [""])[0]
            published = payload.get("published-print") or payload.get(
                "published-online", {}
            )
            date_parts = published.get("date-parts", [[]])[0]
            year = date_parts[0] if date_parts else ""
            authors = "; ".join(
                " ".join(
                    part
                    for part in [author.get("given", ""), author.get("family", "")]
                    if part
                )
                for author in payload.get("author", [])
            )
            metadata_rows.append(
                {
                    "doi": doi.lower(),
                    "role": reference["role"],
                    "title": title,
                    "authors": authors,
                    "year": year,
                    "container": container,
                    "crossref_status": status,
                }
            )
            records.append(
                {
                    "doi": doi.lower(),
                    "url": url,
                    "retrieved_utc": datetime.fromtimestamp(
                        path.stat().st_mtime, tz=timezone.utc
                    )
                    .replace(microsecond=0)
                    .isoformat(),
                    "saved_path": str(path.relative_to(ROOT)),
                    "bytes": path.stat().st_size,
                    "sha256": checksum(path),
                    "usage": "Crossref bibliographic metadata",
                    "status": status,
                }
            )
        else:
            records.append(
                {
                    "doi": doi.lower(),
                    "url": url,
                    "retrieved_utc": datetime.now(timezone.utc)
                    .replace(microsecond=0)
                    .isoformat()
                    if doi.lower() not in existing_times
                    else existing_times[doi.lower()],
                    "saved_path": "",
                    "bytes": 0,
                    "sha256": "",
                    "usage": "Crossref bibliographic metadata",
                    "status": status,
                }
            )
    with LEDGER.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(records[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(records)
    pd_rows = sorted(
        metadata_rows,
        key=lambda row: references.index(
            next(item for item in references if item["doi"].lower() == row["doi"])
        ),
    )
    with METADATA.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(pd_rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(pd_rows)
    landing_path = RAW / "akonga_1987_repository_landing.html"
    akonga_path = RAW / "akonga_1987_rainmaking_rituals.pdf"
    if not landing_path.exists():
        response = requests.get(AKONGA_LANDING_URL, timeout=120)
        response.raise_for_status()
        landing_path.write_bytes(response.content)
    if not akonga_path.exists():
        response = requests.get(AKONGA_PDF_URL, timeout=120)
        response.raise_for_status()
        if not response.content.startswith(b"%PDF"):
            raise ValueError("Akong'a repository bitstream is not a PDF")
        akonga_path.write_bytes(response.content)
    if not akonga_path.read_bytes().startswith(b"%PDF"):
        raise ValueError("Stored Akong'a repository bitstream is not a PDF")
    manual_records = []
    for path, url, status in [
        (
            landing_path,
            AKONGA_LANDING_URL,
            "legacy repository response retained as HTML audit snapshot",
        ),
        (
            akonga_path,
            AKONGA_PDF_URL,
            "verified PDF from institutional repository; absent from Crossref",
        ),
    ]:
        manual_records.append(
            {
                "identifier": "doi:10.14989/68028",
                "url": url,
                "retrieved_utc": datetime.fromtimestamp(
                    path.stat().st_mtime, tz=timezone.utc
                )
                .replace(microsecond=0)
                .isoformat(),
                "saved_path": str(path.relative_to(ROOT)),
                "bytes": path.stat().st_size,
                "sha256": checksum(path),
                "usage": "Kyoto University repository article; scholarly citation",
                "status": status,
            }
        )
    with MANUAL_LEDGER.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=list(manual_records[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(manual_records)
    print(f"Verified {len(metadata_rows)} of {len(references)} DOI records")


if __name__ == "__main__":
    acquire()
