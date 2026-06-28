from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_ai(prompt: str, language: str = "English"):
    system_prompt = f"""
You are an AI Study Assistant.

Rules:
- Explain concepts clearly.
- Answer in {language}.
- Use bullet points whenever useful.
- If the user asks for notes, provide concise study notes.
- If the user asks for code, provide complete working code.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[system_prompt, prompt]
    )

    return response.text
