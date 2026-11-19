"""Fetch and validate JSONPlaceholder posts, then save the first five."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"
OUTPUT_FILE = Path(__file__).with_name("first_five_posts.json")
REQUIRED_KEYS = {"userId", "id", "title", "body"}


def fetch_and_validate_posts() -> list[dict]:
    """Fetch all posts and validate the HTTP status and each post's shape."""
    response = requests.get(API_URL, timeout=30)
    if response.status_code != 200:
        raise RuntimeError(f"Expected HTTP 200, got {response.status_code}")

    posts = response.json()
    if not isinstance(posts, list):
        raise ValueError("Expected the API response to be a JSON array")

    for index, post in enumerate(posts):
        if not isinstance(post, dict):
            raise ValueError(f"Post at index {index} is not a JSON object")
        missing = REQUIRED_KEYS - post.keys()
        if missing:
            raise ValueError(
                f"Post at index {index} is missing required keys: "
                f"{', '.join(sorted(missing))}"
            )
    return posts


def main() -> int:
    try:
        posts = fetch_and_validate_posts()
        first_five = posts[:5]
        OUTPUT_FILE.write_text(
            json.dumps(first_five, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Validated {len(posts)} posts (HTTP 200).")
        print(f"Saved {len(first_five)} posts to {OUTPUT_FILE.name}.")
        return 0
    except (requests.RequestException, ValueError, RuntimeError) as error:
        print(f"API automation failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
