import PyPDF2
from fastapi import UploadFile


async def extract_text_from_pdf(file: UploadFile):
    reader = PyPDF2.PdfReader(file.file)

    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    return text
