import streamlit as st
import google.generativeai as genai
import os
import PyPDF2

# Set up the Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBqKPhSAFFE3PhUDiv3pSwbNKygQQGfCpE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="ThreatGuard", page_icon="🛡️", layout="centered")

st.title("🛡️ ThreatGuard - URL and File Threat Detector")

def predict_fake_or_real_email_content(text):
    prompt = f"""
    You are an expert in identifying scam messages in text, email etc. Analyze the given text and classify it as:

    - Real/Legitimate
    - Scam/Fake

    for the following Text:
    {text}

    Only return the classification message and nothing else.
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Classification failed."

def url_detection(url):
    prompt = f"""
    Analyze the given URL and classify it as:
    - benign
    - phishing
    - malware
    - defacement

    URL: {url}
    """
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Detection failed."

# Tabs for File and URL analysis
tab1, tab2 = st.tabs(["🔍 Analyze File", "🌐 Analyze URL"])

with tab1:
    st.subheader("Malicious File Detection")
    uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=['pdf', 'txt'])
    if uploaded_file:
        extracted_text = ""
        if uploaded_file.name.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        elif uploaded_file.name.endswith('.txt'):
            extracted_text = uploaded_file.read().decode("utf-8")

        if extracted_text.strip():
            result = predict_fake_or_real_email_content(extracted_text)
            st.success(f"**Result:** {result}")
        else:
            st.error("File is empty or could not extract text.")

with tab2:
    st.subheader("URL Threat Detection")
    url = st.text_input("Enter URL (must start with http:// or https://)")
    if st.button("Analyze URL"):
        if url.startswith(('http://', 'https://')):
            classification = url_detection(url)
            st.success(f"**URL:** {url}\n\n**Classification:** {classification}")
        else:
            st.error("Please enter a valid URL starting with http:// or https://")

