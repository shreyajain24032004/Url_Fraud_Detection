 🛡️ ThreatGuard - Security Analyzer

ThreatGuard is a multi-modal security analyzer designed to detect potential threats in URLs and analyze file content for scam/phishing attempts. It utilizes the **Gemini 2.5 Flash model** and the **VirusTotal API** for powerful threat detection.

---

## ✨ Key Features

* **🌐 URL Threat Detection:**
    * Checks URLs against **VirusTotal** for known malicious indicators (phishing, malware).
    * Uses **Gemini 2.5 Flash** as a fallback for smart, AI-powered classification.
* **📄 File Scam Analysis (Streamlit Only):**
    * Analyzes text extracted from **PDF and TXT** files.
    * Classifies content as **"Real/Legitimate"** or **"Scam/Fake"** using Gemini.
* **Interfaces:** Includes a user-friendly **Streamlit App** (`app.py`) and a basic **Flask API** (`main.py`) for URL checking.

---

## ⚙️ Setup and Installation

### Prerequisites

1.  **Python 3.8+**
2.  **API Keys:**
    * **Google AI API Key**
    * **VirusTotal API Key**

### Installation

1.  **Clone the repository and set up a virtual environment.**
2.  **Install dependencies:**
    ```bash
    pip install streamlit flask requests google-genai PyPDF2
    ```

### Configuration

For the app to work, replace the placeholder API keys in both **`app.py`** and **`main.py`** with your actual keys:

```python
# Locate and update these lines in both app.py and main.py:
VT_API_KEY = "YOUR_VIRUSTOTAL_API_KEY" 
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_API_KEY"
````

-----

## 🚀 How to Run

### Option 1: Streamlit Web App (Recommended for File & URL Analysis)

```bash
streamlit run app.py
```

*(Access the app at `http://localhost:8501`)*

### Option 2: Flask API (For URL Detection Integration)

```bash
python main.py
```
