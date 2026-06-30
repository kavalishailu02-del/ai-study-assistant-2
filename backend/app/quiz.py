from dotenv import load_dotenv
from google import genai
import os

load_dotenv()


def generate_quiz(text: str, num_questions: int = 5):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = f"""
Create {num_questions} multiple choice questions from the following content.

{text}
"""

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)

    return response.text
