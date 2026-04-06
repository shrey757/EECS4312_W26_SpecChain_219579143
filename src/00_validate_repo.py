"""checks required files/folders exist"""
from pathlib import Path
import json
import sys

REQUIRED_FILES = [
    "README.md",
    "data/reviews_raw.jsonl",
    "data/reviews_clean.jsonl",
    "data/dataset_metadata.json",
    "data/review_groups_manual.json",
    "data/review_groups_auto.json",
    "data/review_groups_hybrid.json",
    "personas/personas_manual.json",
    "personas/personas_auto.json",
    "personas/personas_hybrid.json",
    "spec/spec_manual.md",
    "spec/spec_auto.md",
    "spec/spec_hybrid.md",
    "tests/tests_manual.json",
    "tests/tests_auto.json",
    "tests/tests_hybrid.json",
    "metrics/metrics_manual.json",
    "metrics/metrics_auto.json",
    "metrics/metrics_hybrid.json",
    "metrics/metrics_summary.json",
    "prompts/prompt_auto.json",
    "reflection/reflection.md",
]

JSON_FILES = [
    "data/dataset_metadata.json",
    "data/review_groups_manual.json",
    "data/review_groups_auto.json",
    "data/review_groups_hybrid.json",
    "personas/personas_manual.json",
    "personas/personas_auto.json",
    "personas/personas_hybrid.json",
    "tests/tests_manual.json",
    "tests/tests_auto.json",
    "tests/tests_hybrid.json",
    "metrics/metrics_manual.json",
    "metrics/metrics_auto.json",
    "metrics/metrics_hybrid.json",
    "metrics/metrics_summary.json",
    "prompts/prompt_auto.json",
]

def check_exists_and_nonempty(path_str: str) -> list[str]:
    errors = []
    path = Path(path_str)
    if not path.exists():
        errors.append(f"Missing required file: {path_str}")
    elif path.is_file() and path.stat().st_size == 0:
        errors.append(f"Empty required file: {path_str}")
    return errors

def check_json_valid(path_str: str) -> list[str]:
    errors = []
    try:
        with open(path_str, "r", encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        errors.append(f"Invalid JSON in {path_str}: {e}")
    return errors

def main() -> int:
    errors: list[str] = []

    for file_path in REQUIRED_FILES:
        errors.extend(check_exists_and_nonempty(file_path))

    for json_path in JSON_FILES:
        if Path(json_path).exists() and Path(json_path).stat().st_size > 0:
            errors.extend(check_json_valid(json_path))

    if errors:
        print("Repository validation failed:\n")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Repository validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())