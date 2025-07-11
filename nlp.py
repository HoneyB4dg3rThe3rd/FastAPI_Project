import logging
import os
from pathlib import Path
from textblob import TextBlob

os.chdir(Path(__file__).parent)

def main():
    text = "Textblob is amazingly simple to use. What great fun!"
    print(text_analysis(text))


def text_analysis(text:str) -> dict: #TODO return value is a special type, no dict
    """Analyses wether some input text is positive, neurtral or negative as well as it's subjectivity

    Args:
        text (str): Text to process

    Returns:
        dict: Results of NLP
    """
    logger = logging.getLogger()
    blob = TextBlob(text)
    logger.info("Text ready for sentiment analysis")
    sentiment_analysis = blob.sentiment
    logger.info("Sentiment analysis sucessful")
    return sentiment_analysis

if __name__ == "__main__":
    main()