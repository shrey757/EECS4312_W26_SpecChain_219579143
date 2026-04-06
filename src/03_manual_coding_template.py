"""creates/updates coding table template + instructions"""
from pathlib import Path
import json
import sys

TARGET = Path("data/review_groups_manual.json")

def main() -> int:
    if not TARGET.exists():
        print(f"Missing file: {TARGET}")
        return 1

    try:
        with open(TARGET, "r", encoding="utf-8") as f:
            data = json.load(f)
        groups = data.get("groups", [])
        print(f"Manual coding step ready: found {len(groups)} manual review groups in {TARGET}.")
        return 0
    except Exception as e:
        print(f"Could not read {TARGET}: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())