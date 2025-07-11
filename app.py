import config as cfg
import os
import streamlit as st
import requests
import logging

from pathlib import Path

__author__ = "HoneyBadger"
__title__ = cfg.APP_TITLE
__version__ = "1.0.0"


os.chdir(Path(__file__).parent)
logging.basicConfig(filename='fastapi.log', level=logging.INFO)
logger = logging.getLogger(__name__)

def create_frontend():
    """creates frontend of app
    """
    st.title("Evaluate Text")
    text = st.text_input("Text to evaluate.")
    logger.info("Received text to evaluate.")
    if st.button("Evaluate"):
        result_blob = post_request(text)
        if result_blob.status_code == 200:
            col1, col2 = st.columns(2)
            logger.info(f"API-request for blob-analyzer successful.")
            result_blob = result_blob.json()
            col1.metric("Polarity", round(result_blob["polarity"], 2))
            col2.metric("Subjectivity", round(result_blob["subjectivity"], 2))
            logger.info(f"\nResults:\n\tInput: {text}\n\tPolarity: {round(result_blob["polarity"], 2)}\n\tSubjectivity: {round(result_blob["subjectivity"], 2)}")
        else:
            logger.info(f"API-request for blob-analyzer failed with code: {result_blob.status_code}")
        
        result_transformer = post_request(text, analyzer="transformer")
        if result_transformer.status_code == 200:
            col1, col2 = st.columns(2)
            logger.info(f"API-request for transfomer-analyzer successful.")
            result_transformer = result_transformer.json()
            col1.metric("Label", result_transformer["label"])
            col2.metric("Polarity", round(result_transformer["score"], 2))
            logger.info(f"\nResults:\n\tInput: {text}\n\tPolarity: {round(result_transformer["score"], 2)}")
        else:
            logger.info(f"API-request for transfomer-analyzer failed with code: {result_transformer.status_code}")


def post_request(input: str, analyzer: str="blob") -> object:
    """sends post request to backend

    Args:
        input (str): string to analyze
        analyzer (str, optional): determines which analyzer is used. Defaults to "blob".

    Returns:
        dict: api-result
    """
    url = f"http://localhost:8000/analyze_{analyzer}"
    data = {"text": input}
    logger.info("Sending API-request...")
    result = requests.post(url, json = data)
    return result

def main():
    create_frontend()

if __name__ =="__main__":
    main()
    logger.info("Application Closed!")