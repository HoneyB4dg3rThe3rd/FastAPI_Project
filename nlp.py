import logging
import os
from pathlib import Path
from textblob import TextBlob
from transformers import pipeline

logging.basicConfig(filename="fastapi.log", level=logging.INFO)
os.chdir(Path(__file__).parent)


def main():
    text = "Textblob is amazingly simple to use. What great fun!"
    print(sentiment_analysis_blob(text))
    print(sentiment_analysis_transformer(text))


def sentiment_analysis_blob(text: str) -> dict:
    """Analyses the polarity of some text as well as it's subjectivity

    Args:
        text (str): Text to process

    Returns:
        dict: Results of NLP
    """
    logger = logging.getLogger()
    blob = TextBlob(text)
    logger.info(
        "Text ready for sentiment analysis [TextBlob]."
    )  # FIXME logging
    sentiment_analysis = {
        "polarity": blob.sentiment.polarity,
        "subjectivity": blob.sentiment.subjectivity,
    }
    logger.info("Sentiment analysis sucessful [TextBlob].")  # FIXME logging
    return sentiment_analysis


def sentiment_analysis_transformer(text: str) -> dict:
    """Analyses the polarity of some text

    Args:
        text (str): Text to process

    Returns:
        dict: Results of NLP
    """
    logger = logging.getLogger()
    sentiment_pipeline = pipeline("sentiment-analysis")
    analysis_results = sentiment_pipeline([text])
    logger.info(
        "Text ready for sentiment analysis [transformer]."
    )  # FIXME logging
    sentiment_analysis_transformer = {
        "label": analysis_results[0]["label"],
        "score": analysis_results[0]["score"],
    }
    logger.info("Sentiment analysis sucessful [transformer].")  # FIXME logging
    return sentiment_analysis_transformer


if __name__ == "__main__":
    main()
