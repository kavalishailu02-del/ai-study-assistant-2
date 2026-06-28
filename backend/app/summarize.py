from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

def summarize_text(text: str):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = f"""
You are an AI Study Assistant.

Summarize the following study material.

Rules:
- Use headings.
- Use bullet points.
- Highlight important concepts.
- Keep it concise.

Study Material:

{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
