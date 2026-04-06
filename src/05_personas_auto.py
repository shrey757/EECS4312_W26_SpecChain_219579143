"""automated persona generation pipeline"""
from pathlib import Path
import json
import sys

PROMPT_FILE = Path("prompts/prompt_auto.json")
TARGET = Path("personas/personas_auto.json")

def main() -> int:
    for path in [PROMPT_FILE, TARGET]:
        if not path.exists():
            print(f"Missing file: {path}")
            return 1

    try:
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            prompt_data = json.load(f)
        with open(TARGET, "r", encoding="utf-8") as f:
            persona_data = json.load(f)

        prompt_present = "prompt" in prompt_data and bool(prompt_data["prompt"])
        persona_count = len(persona_data.get("personas", []))

        print(f"Automated persona step ready: prompt_present={prompt_present}, personas={persona_count}")
        return 0
    except Exception as e:
        print(f"Could not validate automated persona artifacts: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())