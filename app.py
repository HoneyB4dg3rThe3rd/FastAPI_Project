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
        result = post_request(text)
        if result.status_code == 200:
            col1, col2 = st.columns(2)
            logger.info("API-request successful.")
            result = result.json()
            col1.metric("Polarity", round(result["polarity"], 2))
            col2.metric("Subjectivity", round(result["subjectivity"], 2))
            logger.info(f"Results:\n\tInput: {text}\n\tPolarity: {round(result["polarity"], 2)}\n\tSubjectivity: {round(result["subjectivity"], 2)}")
        else:
            logger.info(f"API-request failed with code: {result.status_code}")


def post_request(input: str) -> object:
    """sends post request to backend

    Args:
        input (str): string to analyze

    Returns:
        dict: api-result
    """
    url = "http://localhost:8000/analyze"
    data = {"text": input}
    logger.info("Sending API-request...")
    result = requests.post(url, json = data)
    return result

def main():
    create_frontend()

if __name__ =="__main__":
    main()
    logger.info("Application Closed!")