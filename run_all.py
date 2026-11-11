from __future__ import annotations

import argparse
import csv
import fnmatch
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent
RAW_LEDGERS = [
    ROOT / "data" / "raw" / "acquisition_ledger.csv",
    ROOT / "data" / "raw" / "invalid_acquisition_ledger.csv",
    ROOT / "data" / "raw" / "literature_acquisition_ledger.csv",
]
OPTIONAL_AUDIT_LEDGERS = [
    ROOT / "data" / "raw" / "literature_source_ledger.csv",
    ROOT / "data" / "raw" / "journal_acquisition_ledger.csv",
]
PIPELINE = [
    ("framework diagram", ROOT / "src" / "model_diagram.py"),
    ("weather and pseudo-events", ROOT / "src" / "weather_analysis.py"),
    ("principal Monte Carlo simulation", ROOT / "simulation" / "run_simulation.py"),
    (
        "generic rare-event simulation",
        ROOT / "simulation" / "general_rare_event.py",
    ),
    (
        "look-ahead correction comparison",
        ROOT / "analysis" / "lookahead_correction_diff.py",
    ),
    ("robustness and sensitivity", ROOT / "analysis" / "robustness.py"),
    (
        "figures, tables, and manuscript values",
        ROOT / "analysis" / "build_manuscript_assets.py",
    ),
    ("result traceability", ROOT / "analysis" / "result_traceability.py"),
    ("manuscript package", ROOT / "manuscript" / "build_manuscript.py"),
    ("final statistical and package audit", ROOT / "analysis" / "final_audit.py"),
]
MANIFEST_PATTERNS = [
    "analysis/*.csv",
    "data/processed/*.csv.gz",
    "results/*.csv",
    "results/*.json",
    "results/*.csv.gz",
    "tables/*.csv",
    "manuscript/*.md",
    "manuscript/*.json",
    "supplement/*.md",
]
PACKAGES = [
    "CairoSVG",
    "matplotlib",
    "numpy",
    "pandas",
    "python-docx",
    "python-pptx",
    "PyYAML",
    "reportlab",
    "requests",
    "scipy",
    "seaborn",
    "statsmodels",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


PUBLIC_MIRROR_EXCLUSIONS = ROOT / "config" / "public_mirror_exclusions.txt"


def withheld_patterns() -> list[str]:
    lines = PUBLIC_MIRROR_EXCLUSIONS.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]


def is_withheld(saved_path: str) -> bool:
    return any(fnmatch.fnmatch(saved_path, pattern) for pattern in withheld_patterns())


def validate_ledger(path: Path) -> int:
    if not path.exists():
        raise FileNotFoundError(f"Missing acquisition ledger: {path}")
    checked = 0
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            saved_path = row.get("saved_path", "")
            if not saved_path:
                continue
            source = ROOT / saved_path
            if not source.exists():
                if is_withheld(saved_path):
                    print(f"Not redistributed (config/public_mirror_exclusions.txt): {saved_path}", flush=True)
                    continue
                raise FileNotFoundError(f"Missing raw input: {source}")
            expected_bytes = row.get("bytes", "")
            if expected_bytes and source.stat().st_size != int(expected_bytes):
                raise ValueError(f"Size mismatch for {source}")
            expected_hash = row.get("sha256", "")
            if expected_hash and sha256(source) != expected_hash:
                raise ValueError(f"SHA-256 mismatch for {source}")
            checked += 1
    return checked


def validate_raw_inputs() -> None:
    checked = sum(validate_ledger(path) for path in RAW_LEDGERS)
    checked += sum(
        validate_ledger(path) for path in OPTIONAL_AUDIT_LEDGERS if path.exists()
    )
    akonga = ROOT / "data" / "raw" / "literature" / (
        "akonga_1987_rainmaking_rituals.pdf"
    )
    if akonga.exists() and not akonga.read_bytes().startswith(b"%PDF"):
        raise ValueError("The archived Akong'a source is not a valid PDF")
    print(f"Validated {checked} archived raw-input records", flush=True)


def run_step(label: str, script: Path) -> None:
    started = time.monotonic()
    print(f"[run] {label}", flush=True)
    subprocess.run(
        [sys.executable, str(script)],
        cwd=ROOT,
        env={"PYTHONPATH": str(ROOT), **dict(os.environ)},
        check=True,
    )
    print(f"[done] {label} ({time.monotonic() - started:.1f}s)", flush=True)


def output_files() -> list[Path]:
    files = set()
    for pattern in MANIFEST_PATTERNS:
        files.update(ROOT.glob(pattern))
    return sorted(path for path in files if path.name != "reproduction_manifest.json")


def libreoffice_version() -> str:
    result = subprocess.run(
        ["libreoffice", "--version"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return result.stdout.strip()


def write_manifest() -> None:
    package_versions = {
        package: importlib.metadata.version(package) for package in PACKAGES
    }
    files = [
        {
            "path": str(path.relative_to(ROOT)),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in output_files()
    ]
    payload = {
        "pipeline": [str(script.relative_to(ROOT)) for _, script in PIPELINE],
        "python": platform.python_version(),
        "platform": platform.platform(),
        "libreoffice": libreoffice_version(),
        "packages": package_versions,
        "outputs": files,
    }
    destination = ROOT / "results" / "reproduction_manifest.json"
    destination.write_text(json.dumps(payload, indent=2) + "\n")
    print(
        f"Wrote {destination.relative_to(ROOT)} with {len(files)} output hashes",
        flush=True,
    )


def validate_outputs() -> None:
    metrics = json.loads(
        (ROOT / "manuscript" / "manuscript_metrics.json").read_text()
    )
    if metrics["pages_blinded_pdf"] > 50:
        raise ValueError("JRU may reject manuscripts over 50 pages")
    if not 150 <= metrics["abstract_words"] <= 250:
        raise ValueError("JRU abstracts must have 150-250 words")
    if not 4 <= metrics["keywords"] <= 6:
        raise ValueError("JRU requires 4-6 keywords")
    required = [
        ROOT / "manuscript" / "manuscript_text.docx",
        ROOT / "manuscript" / "manuscript_text.pdf",
        ROOT / "manuscript" / "manuscript_blinded.docx",
        ROOT / "supplement" / "supplement.docx",
        ROOT / "supplement" / "supplement.pdf",
        ROOT / "figures" / "figure1_framework.pdf",
        ROOT / "figures" / "figures_editable.pptx",
        ROOT / "tables" / "main_tables_editable.docx",
        ROOT / "results" / "manuscript_values.json",
        ROOT
        / "manuscript"
        / "pricing_rare_events_jru_submission.zip",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing required outputs: {missing}")


def run_tests() -> None:
    subprocess.run(
        [sys.executable, "-m", "pytest", "tests", "-q"],
        cwd=ROOT,
        env={"PYTHONPATH": str(ROOT), **dict(os.environ)},
        check=True,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rebuild Pricing Apparent Environmental Performance from archived inputs."
        )
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate archived inputs and existing outputs without rebuilding.",
    )
    parser.add_argument(
        "--skip-tests",
        action="store_true",
        help="Skip the final pytest verification.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    validate_raw_inputs()
    if not args.validate_only:
        for label, script in PIPELINE:
            run_step(label, script)
        write_manifest()
    validate_outputs()
    if not args.skip_tests:
        run_tests()
    print("Reproducibility pipeline completed successfully", flush=True)


if __name__ == "__main__":
    main()
