from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Study Assistant API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


@app.get("/")
def home():
    return {"message": "AI Study Assistant Backend is Running"}


@app.post("/ask")
async def ask(question: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=question
        )

        return {"answer": response.text}

    except Exception as e:
        return {"error": str(e)}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "File uploaded successfully"}
