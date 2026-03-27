"""imports or reads your raw dataset; if you scraped, include scraper here"""
from google_play_scraper import reviews, Sort
import json
import os
from datetime import datetime

APP_ID = "bot.touchkin"
OUTPUT_PATH = "data/reviews_raw.jsonl"
TARGET_COUNT = 2000

def ensure_data_dir():
    os.makedirs("data", exist_ok=True)

def serialize_datetime(value):
    if isinstance(value, datetime):
        return value.isoformat()
    return str(value)

def main():
    ensure_data_dir()

    all_reviews = []
    continuation_token = None

    while len(all_reviews) < TARGET_COUNT:
        batch, continuation_token = reviews(
            APP_ID,
            lang="en",
            country="ca",
            sort=Sort.NEWEST,
            count=min(200, TARGET_COUNT - len(all_reviews)),
            continuation_token=continuation_token
        )

        if not batch:
            break

        all_reviews.extend(batch)

        if continuation_token is None:
            break

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        for idx, review in enumerate(all_reviews, start=1):
            row = {
                "id": f"r{idx}",
                "reviewId": review.get("reviewId", ""),
                "appId": APP_ID,
                "userName": review.get("userName", ""),
                "score": review.get("score", None),
                "content": review.get("content", ""),
                "at": serialize_datetime(review.get("at", "")),
                "thumbsUpCount": review.get("thumbsUpCount", 0),
                "source": "google_play"
            }
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Saved {len(all_reviews)} raw reviews to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
