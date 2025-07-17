import json
from pathlib import Path
from typing import Any, Dict, List


def load_json(path: Path) -> Dict[str, Any]:
    """Load JSON data from a file."""
    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_json(data: Dict[str, Any], path: Path) -> None:
    """Save JSON data to a file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def load_users(path: Path) -> List[Dict[str, Any]]:
    """Load a list of users from the given path."""
    data = load_json(path)
    return data.get("users", [])


def save_users(users: List[Dict[str, Any]], path: Path) -> None:
    """Save a list of users to the given path."""
    save_json({"users": users}, path)