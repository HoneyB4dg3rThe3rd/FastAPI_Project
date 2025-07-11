import logging
import os
from pathlib import Path
from textblob import TextBlob

os.chdir(Path(__file__).parent)

def main():
    text = "Textblob is amazingly simple to use. What great fun!"
    print(sentiment_analysis(text))


def sentiment_analysis(text:str) -> dict:
    """Analyses the polarity of some text as well as it's subjectivity

    Args:
        text (str): Text to process

    Returns:
        dict: Results of NLP
    """
    logger = logging.getLogger()
    blob = TextBlob(text)
    logger.info("Text ready for sentiment analysis")
    sentiment_analysis = {
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity
        }
    logger.info("Sentiment analysis sucessful")
    return sentiment_analysis

if __name__ == "__main__":
    main()