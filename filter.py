KEYWORDS = [
    "launch", "launched", "released", "announced",
    "AI", "model", "LLM",
    "phone", "smartphone", "laptop"
]

def is_relevant(article):
    text = (article["title"] + " " + article["summary"]).lower()

    return any(keyword.lower() in text for keyword in KEYWORDS)


def filter_articles(articles):
    return [article for article in articles if is_relevant(article)]