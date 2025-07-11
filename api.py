from fastapi import FastAPI
from nlp import sentiment_analysis_blob, sentiment_analysis_transformer
from pydantic import BaseModel

class Text(BaseModel):
    text: str

app = FastAPI()

@app.post("/analyze_blob/")
async def analyse_text_blob(text: Text):
    return sentiment_analysis_blob(text.text)

@app.post("/analyze_transformer/")
async def analyse_text_transformer(text: Text):
    return sentiment_analysis_transformer(text.text)
