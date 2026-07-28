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

    # WordPress article cards usually use article tags
    for post in soup.find_all("article"):

        title_tag = post.find("h2") or post.find("h3")
        link_tag = post.find("a")

        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            link = link_tag.get("href")

            if link:
                articles.append(
                    {
                        "title": title,
                        "link": link,
                        "description": f"Article by Corey Cesare: {title}",
                        "date": ""
                    }
                )

    return articles


if __name__ == "__main__":
    for article in get_articles():
        print(article)
