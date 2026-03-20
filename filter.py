KEYWORDS = [
    "launch", "launched", "released", "announced"
]

GADGET_KEYWORDS = [
    "phone", "smartphone", "laptop", "tablet", "iphone", "samsung", "oneplus", "xiaomi"
]

INDIA_KEYWORDS = [
    "india", "rs", "₹", "inr", "INR", "RS", "Rs"
]


def is_relevant(article):
    text = (article["title"] + " " + article["summary"]).lower()

    # Condition 1: Must be a launch-type news
    is_launch = any(word in text for word in KEYWORDS)

    # Condition 2: Must be a gadget
    is_gadget = any(word in text for word in GADGET_KEYWORDS)

    # Condition 3: Must be India-specific
    is_india = any(word in text for word in INDIA_KEYWORDS)

    return is_launch and is_gadget and is_india


def filter_articles(articles):
    return [article for article in articles if is_relevant(article)]