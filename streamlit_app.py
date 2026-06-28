import streamlit as st
import google.generativeai as genai
import PyPDF2

st.set_page_config(page_title="AI Study Assistant", page_icon="📚")

st.title("📚 AI Study Assistant with PDF")

# API Key
api_key = st.text_input("Enter Gemini API Key", type="password")

# -------------------------------
# Language Selection
# -------------------------------
languages = {
    "English": "English",
    "తెలుగు (Telugu)": "Telugu",
    "हिन्दी (Hindi)": "Hindi",
    "தமிழ் (Tamil)": "Tamil",
    "ಕನ್ನಡ (Kannada)": "Kannada",
    "മലയാളം (Malayalam)": "Malayalam",
    "বাংলা (Bengali)": "Bengali",
    "ગુજરાતી (Gujarati)": "Gujarati",
    "मराठी (Marathi)": "Marathi",
    "ਪੰਜਾਬੀ (Punjabi)": "Punjabi",
    "اردو (Urdu)": "Urdu",
    "Español (Spanish)": "Spanish",
    "Français (French)": "French",
    "Deutsch (German)": "German",
    "日本語 (Japanese)": "Japanese",
    "中文 (Chinese)": "Chinese",
    "한국어 (Korean)": "Korean",
    "Русский (Russian)": "Russian",
    "Português (Portuguese)": "Portuguese",
    "Italiano (Italian)": "Italian"
}

selected_language = st.selectbox(
    "🌍 Select Answer Language",
    list(languages.keys())
)

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

pdf_text = ""

if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text

    st.success("✅ PDF uploaded successfully!")

question = st.text_area("Ask a question about the PDF")

if st.button("Generate Answer"):

    if not api_key:
        st.warning("Please enter Gemini API Key.")
        st.stop()

    if not uploaded_file:
        st.warning("Please upload a PDF.")
        st.stop()

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are an AI Study Assistant.

Study Material:
{pdf_text}

Question:
{question}

Instructions:
1. Answer ONLY using the PDF content.
2. If the answer is unavailable, say:
   "The answer is not available in the uploaded document."
3. Give the answer in {languages[selected_language]}.
4. Explain clearly with headings and bullet points whenever possible.
"""

    with st.spinner("Generating answer..."):
        response = model.generate_content(prompt)

    st.subheader(f"📖 Answer ({selected_language})")
    st.write(response.text)

st.markdown("---")
st.caption("Powered by Gemini 2.5 Flash")
