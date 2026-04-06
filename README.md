# EECS4312_W26_SpecChain

## Application
Wysa

## Data Collection Method
The reviews were collected from the Google Play Store for the Wysa app using a Python script (`src/01_collect_or_import.py`) with the `google-play-scraper` library.

## Original Dataset
- `data/reviews_raw.jsonl` contains the raw collected reviews.
- The raw dataset contains **2000 reviews**.

## Final Cleaned Dataset
- `data/reviews_clean.jsonl` contains the cleaned review dataset.
- The cleaned dataset contains **1650 reviews**.
- Cleaning included duplicate removal, empty/short review removal, lowercasing, URL removal, punctuation/special character removal, emoji removal, number-to-word conversion, stop-word removal, and lemmatization.

## Repository Structure
- `data/` contains datasets, metadata, and review grouping files
- `personas/` contains manual, automated, and hybrid persona files
- `spec/` contains manual, automated, and hybrid requirement specifications
- `tests/` contains manual, automated, and hybrid test files
- `metrics/` contains the metric files and summary comparison
- `prompts/` contains the automated prompt used for generation
- `src/` contains Python scripts for validation, collection/import, cleaning, and pipeline execution
- `reflection/` contains the final reflection file

## Exact Commands to Run Pipeline
1. `python src/00_validate_repo.py`
2. `python src/01_collect_or_import.py`
3. `python src/02_clean.py`
4. `python src/run_all.py`

## Notes
- This project analyzes user reviews of the Wysa mental health app.
- The repository includes three pipelines: manual, automated, and hybrid.
- Comparison results can be found in `metrics/metrics_summary.json`.

