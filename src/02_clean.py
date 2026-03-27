import json
import os
import re
import subprocess
import sys

RAW_PATH = "data/reviews_raw.jsonl"
CLEAN_PATH = "data/reviews_clean.jsonl"
META_PATH = "data/dataset_metadata.json"
MIN_WORDS = 3


def ensure_package(package_name, import_name=None):
    if import_name is None:
        import_name = package_name
    try:
        __import__(import_name)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])


ensure_package("nltk")
ensure_package("num2words")
ensure_package("emoji")

import nltk
import emoji
from num2words import num2words
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords", quiet=True)
nltk.download("wordnet", quiet=True)
nltk.download("omw-1.4", quiet=True)

STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def save_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def remove_emojis(text):
    return emoji.replace_emoji(text, replace="")


def convert_numbers_to_words(text):
    def repl(match):
        try:
            return " " + num2words(int(match.group())) + " "
        except Exception:
            return " "
    return re.sub(r"\b\d+\b", repl, text)


def normalize_text(text):
    text = text.strip()
    text = remove_emojis(text)
    text = text.lower()
    text = convert_numbers_to_words(text)
    text = re.sub(r"http\S+|www\S+", " ", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def tokenize_clean_lemmatize(text):
    tokens = text.split()
    tokens = [t for t in tokens if t not in STOP_WORDS]
    tokens = [LEMMATIZER.lemmatize(t) for t in tokens]
    return tokens


def main():
    os.makedirs("data", exist_ok=True)

    raw_reviews = load_jsonl(RAW_PATH)
    raw_count = len(raw_reviews)

    seen_review_ids = set()
    seen_contents = set()

    clean_rows = []

    duplicate_reviewid_count = 0
    duplicate_text_count = 0
    empty_count = 0
    short_count = 0

    for row in raw_reviews:
        review_id = row.get("reviewId", "").strip()
        original_text = row.get("content", "")

        if review_id and review_id in seen_review_ids:
            duplicate_reviewid_count += 1
            continue
        if review_id:
            seen_review_ids.add(review_id)

        if not original_text or not original_text.strip():
            empty_count += 1
            continue

        normalized = normalize_text(original_text)

        if not normalized:
            empty_count += 1
            continue

        if normalized in seen_contents:
            duplicate_text_count += 1
            continue
        seen_contents.add(normalized)

        tokens = tokenize_clean_lemmatize(normalized)

        if len(tokens) < MIN_WORDS:
            short_count += 1
            continue

        cleaned_text = " ".join(tokens)

        out_row = {
            "id": row.get("id"),
            "reviewId": row.get("reviewId"),
            "appId": row.get("appId"),
            "score": row.get("score"),
            "at": row.get("at"),
            "raw_content": original_text,
            "clean_content": cleaned_text,
            "source": row.get("source", "google_play")
        }
        clean_rows.append(out_row)

    save_jsonl(CLEAN_PATH, clean_rows)

    metadata = {
        "app_name": "Wysa",
        "app_id": "bot.touchkin",
        "store": "Google Play",
        "collection_method": "Collected using google-play-scraper in src/01_collect_or_import.py",
        "raw_dataset_file": "data/reviews_raw.jsonl",
        "clean_dataset_file": "data/reviews_clean.jsonl",
        "raw_dataset_size": raw_count,
        "clean_dataset_size": len(clean_rows),
        "cleaning_decisions": [
            "Removed duplicate reviews based on reviewId.",
            "Removed duplicate reviews based on normalized text content.",
            "Removed empty reviews.",
            "Removed very short reviews with fewer than 3 words after preprocessing.",
            "Converted text to lowercase.",
            "Removed URLs.",
            "Removed punctuation and special characters.",
            "Removed emojis.",
            "Converted numbers to words.",
            "Removed stop words.",
            "Applied lemmatization."
        ],
        "cleaning_summary": {
            "duplicates_by_reviewId_removed": duplicate_reviewid_count,
            "duplicates_by_text_removed": duplicate_text_count,
            "empty_removed": empty_count,
            "short_removed": short_count
        }
    }

    with open(META_PATH, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    print(f"Raw reviews: {raw_count}")
    print(f"Clean reviews: {len(clean_rows)}")
    print(f"Saved cleaned dataset to {CLEAN_PATH}")
    print(f"Saved metadata to {META_PATH}")


if __name__ == "__main__":
    main()