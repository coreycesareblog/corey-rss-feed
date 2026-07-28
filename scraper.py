import requests
from html import unescape


POSTS_URL = "https://talentrecap.com/wp-json/wp/v2/posts"


def get_articles():
    response = requests.get(
        POSTS_URL,
        params={
            "author": 55,
            "per_page": 10,
            "orderby": "date",
            "order": "desc"
        }
    )

    response.raise_for_status()

    posts = response.json()

    articles = []

    for post in posts:
        articles.append(
            {
                "title": unescape(post["title"]["rendered"]),
                "link": post["link"],
                "description": unescape(
                    post["excerpt"]["rendered"]
                ),
                "date": post["date"]
            }
        )

    print(f"Found {len(articles)} articles")

    for article in articles:
        print(article["title"])

    return articles


if __name__ == "__main__":
    get_articles()
