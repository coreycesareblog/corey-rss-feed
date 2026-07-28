import requests


SEARCH_URL = "https://talentrecap.com/wp-json/wp/v2/search"


def get_articles():
    response = requests.get(
        SEARCH_URL,
        params={
            "search": "Corey Cesare",
            "per_page": 10
        }
    )

    response.raise_for_status()

    posts = response.json()

    articles = []

    for post in posts:
        if post.get("subtype") == "post":

            articles.append(
                {
                    "title": post["title"],
                    "link": post["url"],
                    "description": f"Article by Corey Cesare: {post['title']}",
                    "date": ""
                }
            )

    print(f"Found {len(articles)} articles")

    for article in articles:
        print(article["title"])

    return articles


if __name__ == "__main__":
    get_articles()
