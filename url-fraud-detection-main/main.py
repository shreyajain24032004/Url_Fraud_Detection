from flask import Flask, render_template, request
import google.generativeai as genai
import os
import PyPDF2

app = Flask(__name__)

# Set up the Google API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyBqKPhSAFFE3PhUDiv3pSwbNKygQQGfCpE"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")

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


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/scam/', methods=['GET', 'POST'])
def detect_scam():
    if request.method == 'GET':
        return render_template("index.html")

    if 'file' not in request.files:
        return render_template("index.html", message="No file uploaded.")

    file = request.files['file']
    extracted_text = ""

    if file.filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    elif file.filename.endswith('.txt'):
        extracted_text = file.read().decode("utf-8")
    else:
        return render_template("index.html", message="Invalid file type. Please upload a PDF or TXT file.")

    if not extracted_text.strip():
        return render_template("index.html", message="File is empty or text could not be extracted.")

    message = predict_fake_or_real_email_content(extracted_text)
    return render_template("index.html", message=message)


@app.route('/predict', methods=['GET', 'POST'])
def predict_url():
    if request.method == 'GET':
        return render_template("index.html")

    url = request.form.get('url', '').strip()

    if not url.startswith(("http://", "https://")):
        return render_template("index.html", message="Invalid URL format.", input_url=url)

    classification = url_detection(url)
    return render_template("index.html", input_url=url, predicted_class=classification)


if __name__ == '__main__':
    app.run(debug=True)
