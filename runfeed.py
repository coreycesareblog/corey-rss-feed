from scraper import get_articles
from generate_feed import generate_feed

articles = get_articles()

generate_feed(articles)

print(f"Generated feed with {len(articles)} articles")
