import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import os
from dotenv import load_dotenv
from groq import Groq
import csv

# Page config
st.set_page_config(page_title="ICD Code Predictor", page_icon="💊")

# UI header
st.title("💊 ICD Code Predictor")
st.write("Enter a diagnosis below to get the ICD-10 code prediction.")

# Load dataset
df = pd.read_csv("data/icd_dataset.csv", encoding="utf-8")
X = df["Diagnosis"]
y = df["ICD_Code"]

# Train model
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)
model = LogisticRegression()
model.fit(X_vec, y)

# Load Groq key
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def groq_icd_lookup(diagnosis):
    prompt = f"Provide the ICD-10 code for: {diagnosis}"
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def append_to_dataset(diagnosis, icd_code):
    with open("data/icd_dataset.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([diagnosis, icd_code])

# Input box
diagnosis = st.text_input("Enter diagnosis:")

if diagnosis:
    sample_vec = vectorizer.transform([diagnosis])
    prediction = model.predict(sample_vec)[0]

    if prediction not in df["ICD_Code"].values:
        st.warning("Not found in dataset. Querying Groq...")
        groq_result = groq_icd_lookup(diagnosis)
        st.info(f"Groq result: {groq_result}")
        append_to_dataset(diagnosis, groq_result)
        st.success("New ICD code added to dataset!")
    else:
        st.success(f"Predicted ICD Code: {prediction}")
