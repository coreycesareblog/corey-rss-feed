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

    # Look through all links on the author page
    for link in soup.find_all("a", href=True):
        url = link["href"]
        title = link.get_text(strip=True)

        # Only collect actual article links
        if (
            "talentrecap.com" in url
            and title
            and "/author/" not in url
            and url.rstrip("/") != AUTHOR_URL.rstrip("/")
        ):
            articles.append(
                {
                    "title": title,
                    "link": url,
                    "description": f"Article by Corey Cesare: {title}",
                    "date": ""
                }
            )

    # Remove duplicates
    unique_articles = []
    seen = set()

    for article in articles:
        if article["link"] not in seen:
            seen.add(article["link"])
            unique_articles.append(article)

    return unique_articles[:10]


if __name__ == "__main__":
    articles = get_articles()

    print(f"Found {len(articles)} articles")

    for article in articles:
        print(article)
