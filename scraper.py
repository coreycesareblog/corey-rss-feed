import requests
from bs4 import BeautifulSoup


AUTHOR_URL = "https://talentrecap.com/author/corey-cesare/"


def get_articles():
    response = requests.get(
        AUTHOR_URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    articles = []

    # Find article containers
    for article in soup.find_all("article"):
        title = None
        link = None

        heading = article.find(["h1", "h2", "h3"])

        if heading:
            title = heading.get_text(strip=True)

            link_tag = heading.find("a")

            if link_tag:
                link = link_tag.get("href")

        if title and link:
            articles.append(
                {
                    "title": title,
                    "link": link,
                    "description": f"Article by Corey Cesare: {title}",
                    "date": ""
                }
            )

    print(f"Found {len(articles)} articles")

    for article in articles:
        print(article["title"])

    return articles


if __name__ == "__main__":
    get_articles()
