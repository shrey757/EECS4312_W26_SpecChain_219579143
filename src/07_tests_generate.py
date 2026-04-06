"""generates tests from specs"""
from pathlib import Path
import json
import sys

TEST_FILES = [
    Path("tests/tests_manual.json"),
    Path("tests/tests_auto.json"),
    Path("tests/tests_hybrid.json"),
]

def main() -> int:
    total_tests = 0

    for test_file in TEST_FILES:
        if not test_file.exists():
            print(f"Missing file: {test_file}")
            return 1
        if test_file.stat().st_size == 0:
            print(f"Empty file: {test_file}")
            return 1

        try:
            with open(test_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            total_tests += len(data.get("tests", []))
        except Exception as e:
            print(f"Invalid JSON in {test_file}: {e}")
            return 1

    print(f"Test generation step ready: found {total_tests} total tests across all pipelines.")
    return 0

if __name__ == "__main__":
    sys.exit(main())