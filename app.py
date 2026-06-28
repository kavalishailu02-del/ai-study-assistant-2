from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
import os

from app.ai import ask_ai
from app.pdf_reader import extract_text
from app.summarize import summarize_file
from app.quiz import generate_quiz

app = FastAPI(title="AI Study Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class ChatRequest(BaseModel):
    prompt: str
    api_key: str


@app.get("/")
def home():
    return {
        "status": "running",
        "project": "AI Study Assistant"
    }


@app.post("/chat")
def chat(request: ChatRequest):
    answer = ask_ai(request.prompt, request.api_key)

    return {
        "response": answer
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }


@app.get("/read/{filename}")
def read_pdf(filename: str):

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    text = extract_text(path)

    return {
        "text": text
    }


@app.post("/summary")
def summary(
    filename: str = Form(...),
    api_key: str = Form(...)
):

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    result = summarize_file(path, api_key)

    return {
        "summary": result
    }


@app.post("/quiz")
def quiz(
    filename: str = Form(...),
    api_key: str = Form(...)
):

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    result = generate_quiz(path, api_key)

    return {
        "quiz": result
    }
