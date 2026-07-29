from scraper import get_articles
from generate_feed import create_feed

articles = get_articles()

create_feed(articles)

print(f"Generated feed with {len(articles)} articles")
