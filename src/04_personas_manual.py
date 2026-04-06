from pathlib import Path
import json
import sys

TARGET = Path("personas/personas_manual.json")

def main() -> int:
    if not TARGET.exists():
        print(f"Missing file: {TARGET}")
        return 1

    try:
        with open(TARGET, "r", encoding="utf-8") as f:
            data = json.load(f)
        personas = data.get("personas", [])
        print(f"Manual persona step ready: found {len(personas)} personas in {TARGET}.")
        return 0
    except Exception as e:
        print(f"Could not read {TARGET}: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())