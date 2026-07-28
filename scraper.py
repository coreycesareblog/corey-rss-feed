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

    print("PAGE TITLE:")
    print(soup.title)

    print("\nFIRST 20 LINKS FOUND:")
    count = 0

    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        url = link["href"]

        if title:
            print(title, "→", url)
            count += 1

        if count >= 20:
            break

    return []


if __name__ == "__main__":
    get_articles()
