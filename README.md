

```markdown
# 💊 ICD Code Predictor

A Streamlit web application that predicts **ICD-10 codes** from medical diagnoses.  
It uses a trained machine learning model on a local dataset, and if the ICD code is not found, it queries **Groq AI** as a fallback. The app also auto‑learns by saving new ICD codes into the dataset.

---

## 🚀 Features
- Predict ICD codes from diagnosis text using **Logistic Regression**.
- **Groq fallback**: if the code isn’t in the dataset, Groq suggests one.
- **Auto‑learning**: new ICD codes are appended to the dataset automatically.
- **Colorful Streamlit UI** with sidebar info and styled result boxes.

---

## 📂 Project Structure
```
healthcare_icd_ai/
├── app/
│   └── icd_app.py        # Streamlit app
├── data/
│   └── icd_dataset.csv   # Dataset of diagnoses and ICD codes
├── models/               # (optional future models)
├── notebooks/            # Training experiments
├── venv/                 # Virtual environment
└── requirements.txt      # Dependencies
```

---

## ⚙️ Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/yourusername/healthcare_icd_ai.git
cd healthcare_icd_ai
pip install -r requirements.txt
```

---

## 🧪 Run Locally
Start the Streamlit app:

```bash
streamlit run app/icd_app.py
```

Then open `http://localhost:8501` [(localhost in Bing)](https://www.bing.com/search?q="http%3A%2F%2Flocalhost%3A8501%2F") in your browser.

---

## 🔑 Environment Variables
Set your **Groq API key** as an environment variable:

```bash
export GROQ_API_KEY="your_actual_key_here"
```

On Windows PowerShell:

```powershell
$env:GROQ_API_KEY="your_actual_key_here"
```

---

## 🌐 Deploy on Streamlit Cloud
1. Push this repo to GitHub.  
2. Go to Streamlit Cloud.  
3. Connect your GitHub account and select this repo.  
4. Set the entry point to `app/icd_app.py`.  
5. Add your Groq API key in **Secrets**:
   ```toml
   GROQ_API_KEY="your_actual_key_here"
   ```

---

## 📝 Example Diagnoses
Try these in the app:
- **Asthma** → J45.909  
- **Diabetes** → E11.9  
- **Hypertension** → I10  
- **Migraine** → Groq fallback → G43.909  

---

