import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("../data/icd_dataset.csv", encoding="utf-8")

print("Dataset loaded:")
print(df)

# Prepare features and labels
X = df["Diagnosis"]
y = df["ICD_Code"]

# Convert text to numeric features
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# Train simple classifier
model = LogisticRegression()
model.fit(X_vec, y)

# Test prediction
sample = ["Patient diagnosed with Asthma"]
sample_vec = vectorizer.transform(sample)
print("Predicted ICD Code:", model.predict(sample_vec)[0])
