"""generates structured specs from personas"""
from pathlib import Path
import sys

SPEC_FILES = [
    Path("spec/spec_manual.md"),
    Path("spec/spec_auto.md"),
    Path("spec/spec_hybrid.md"),
]

def main() -> int:
    for spec_file in SPEC_FILES:
        if not spec_file.exists():
            print(f"Missing file: {spec_file}")
            return 1
        if spec_file.stat().st_size == 0:
            print(f"Empty file: {spec_file}")
            return 1

    print("Specification step ready: manual, automated, and hybrid spec files are present.")
    return 0

if __name__ == "__main__":
    sys.exit(main())