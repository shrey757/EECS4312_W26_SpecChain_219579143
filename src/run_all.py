"""runs the full pipeline end-to-end"""
import subprocess
import sys

SCRIPTS = [
    "src/00_validate_repo.py",
    "src/01_collect_or_import.py",
    "src/02_clean.py",
    "src/03_manual_coding_template.py",
    "src/04_personas_manual.py",
    "src/05_personas_auto.py",
    "src/06_spec_generate.py",
    "src/07_tests_generate.py",
    "src/08_metrics.py",
]

def run_step(script_path: str) -> None:
    print(f"\n=== Running {script_path} ===")
    subprocess.run([sys.executable, script_path], check=True)

def main() -> int:
    try:
        for script in SCRIPTS:
            run_step(script)
        print("\nFull pipeline completed successfully.")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"\nPipeline failed while running: {e.cmd}")
        return e.returncode if isinstance(e.returncode, int) else 1

if __name__ == "__main__":
    sys.exit(main())