from rss_fetcher import fetch_articles
from filter import filter_articles
from email_sender import send_email


def run():
    print("Fetching articles...")
    articles = fetch_articles()

    print(f"Total articles fetched: {len(articles)}")

    relevant_articles = filter_articles(articles)

    print(f"Relevant articles found: {len(relevant_articles)}")

    send_email(relevant_articles)


if __name__ == "__main__":
    run()