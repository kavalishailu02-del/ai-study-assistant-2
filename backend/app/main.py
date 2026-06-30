from fastapi import FastAPI, UploadFile, File, Form

from backend.app.pdf_reader import extract_text_from_pdf
from backend.app.summarize import summarize_text
from backend.app.quiz import generate_quiz
from backend.app.translator import translate_text

app = FastAPI()


@app.get("/")
def home():
    return {"message": "AI Study Assistant Backend Running 🚀"}


@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    text = await extract_text_from_pdf(file)
    return {"text": text}


@app.post("/summarize/")
def summarize(text: str = Form(...)):
    return {"summary": summarize_text(text)}


@app.post("/quiz/")
def quiz(text: str = Form(...), num_questions: int = 5):
    return {"quiz": generate_quiz(text, num_questions)}


@app.post("/translate/")
def translate(text: str = Form(...), language: str = "english"):
    return {"translation": translate_text(text, language)}
