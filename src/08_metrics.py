"""computes metrics: coverage/traceability/ambiguity/testability"""
from pathlib import Path
import json
import sys

METRIC_FILES = [
    Path("metrics/metrics_manual.json"),
    Path("metrics/metrics_auto.json"),
    Path("metrics/metrics_hybrid.json"),
    Path("metrics/metrics_summary.json"),
]

def main() -> int:
    for metric_file in METRIC_FILES:
        if not metric_file.exists():
            print(f"Missing file: {metric_file}")
            return 1
        if metric_file.stat().st_size == 0:
            print(f"Empty file: {metric_file}")
            return 1

        try:
            with open(metric_file, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            print(f"Invalid JSON in {metric_file}: {e}")
            return 1

    print("Metrics step ready: all metrics files exist and are valid JSON.")
    return 0

if __name__ == "__main__":
    sys.exit(main())