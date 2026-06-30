from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

SUPPORTED_LANGUAGES = ["english", "hindi", "telugu"]


def translate_text(text: str, target_language: str = "english"):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    if target_language.lower() not in SUPPORTED_LANGUAGES:
        return "Unsupported language."

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Translate the following into {target_language}:\n\n{text}",
    )

    return response.text
