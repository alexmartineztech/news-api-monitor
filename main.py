import os
import requests
from dotenv import load_dotenv

load_dotenv()

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")

BASE_URL = "https://newsapi.org/v2/everything"


def get_news(query):
    params = {
        "q": query,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 5
    }

    headers = {
        "Authorization": NEWSAPI_KEY
    }

    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code != 200:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

    return response.json()


def display_news(articles):
    print("\n🔥 Latest News:\n")

    for i, article in enumerate(articles, start=1):
        title = article.get("title")
        url = article.get("url")

        print(f"{i}. {title}")
        print(f"   {url}\n")


def main():
    topic = input("Enter topic (e.g. technology, AI, bitcoin): ")

    print(f"\nFetching news for: {topic}...\n")

    data = get_news(topic)
    articles = data.get("articles", [])

    if not articles:
        print("No articles found.")
        return

    display_news(articles)


if __name__ == "__main__":
    main()
