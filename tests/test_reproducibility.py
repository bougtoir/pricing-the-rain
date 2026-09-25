import hashlib
import inspect
import json
from pathlib import Path

import run_all
from src import acquire_weather


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def test_archived_raw_inputs_match_ledgers() -> None:
    run_all.validate_raw_inputs()


def test_default_pipeline_is_offline_and_ordered() -> None:
    scripts = [path.relative_to(ROOT).as_posix() for _, path in run_all.PIPELINE]
    assert scripts == [
        "src/model_diagram.py",
        "src/weather_analysis.py",
        "simulation/run_simulation.py",
        "analysis/robustness.py",
        "analysis/build_manuscript_assets.py",
        "manuscript/build_manuscript.py",
        "analysis/final_audit.py",
    ]
    assert all("acquire" not in script for script in scripts)


def test_acquisition_has_no_overwrite_switch() -> None:
    assert not inspect.signature(acquire_weather.acquire).parameters


def test_reproduction_manifest_matches_outputs() -> None:
    manifest = json.loads(
        (ROOT / "results" / "reproduction_manifest.json").read_text()
    )
    for record in manifest["outputs"]:
        path = ROOT / record["path"]
        assert path.stat().st_size == record["bytes"]
        assert sha256(path) == record["sha256"]
