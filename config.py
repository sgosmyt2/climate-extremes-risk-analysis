import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DATA_ROOT = PROJECT_ROOT / "data"

def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

def get_dataset_dir(country: str, dataset: str):
    return DATA_ROOT / country / dataset

def get_raw_dir(country: str, dataset: str):
    return ensure_dir(get_dataset_dir(country, dataset) / "raw")

def get_event_dir(country: str, dataset: str, event: str):
    if event not in {"baseline", "primaryevent"}:
        raise ValueError("event must be 'baseline' or 'primaryevent'")
    return ensure_dir(get_dataset_dir(country, dataset) / event)