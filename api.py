from fastapi import FastAPI
from nlp import sentiment_analysis
from pydantic import BaseModel

class Text(BaseModel):
    text: str

app = FastAPI()

@app.post("/sentimentanalysis")
def analyse_text(text: Text):
    return sentiment_analysis(text.text)
