# project/app/summarizer.py


import nltk
from newspaper import Article


def generate_summary(url: str) -> str:
    article = Article(url)
    print("Article URL")
    article.download()
    print("Article Download")
    article.parse()
    print("Article parse")

    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")
    finally:
        article.nlp()
    print("Article parse")
    return article.summary