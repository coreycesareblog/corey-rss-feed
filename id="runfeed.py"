from scraper import get_articles
from generate_feed import create_feed
from datetime import datetime, timezone


def format_date(article):
    # Placeholder date for now; we'll improve this once we confirm
    # Talent Recap exposes dates cleanly.
    return datetime.now(timezone.utc).strftime(
        "%a, %d %b %Y %H:%M:%S GMT"
    )


articles = get_articles()

for article in articles:
    article["date"] = format_date(article)

create_feed(articles)

print(f"Generated feed with {len(articles)} articles.")
