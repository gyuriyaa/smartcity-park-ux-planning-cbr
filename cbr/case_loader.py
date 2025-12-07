import json
from pathlib import Path
from typing import Any, Dict, List


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "case_base.json"


def load_case_base(path: Path | None = None) -> List[Dict[str, Any]]:
    """
    Load the case base from a JSON file.

    Returns:
        List of case dictionaries.
    """
    file_path = path or DATA_PATH
    if not file_path.exists():
        raise FileNotFoundError(f"Case base file not found: {file_path}")

    with file_path.open(encoding="utf-8") as f:
        return json.load(f)


def save_case_base(case_base: List[Dict[str, Any]], path: Path | None = None) -> None:
    """
    Save the case base back to a JSON file.
    """
    file_path = path or DATA_PATH
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open("w", encoding="utf-8") as f:
        json.dump(case_base, f, indent=2, ensure_ascii=False)
