from fastapi import UploadFile
from PyPDF2 import PdfReader


async def extract_text_from_pdf(file: UploadFile):
    reader = PdfReader(file.file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
