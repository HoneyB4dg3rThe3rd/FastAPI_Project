import json
import logging
import os
from pathlib import Path
from logging.config import fileConfig

os.chdir(Path(__file__).parent)

fileConfig("./logging.ini")


logger = logging.getLogger()

logger.info("Configuartion loading..")

with open("./config.json", mode="r", encoding="UTF-8") as file:
    cfg = json.load(file)

APP_TITLE = cfg["application"]