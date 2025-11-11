# 📱 SMS Spam Detector

A lightweight NLP-powered Streamlit app that classifies SMS messages as **spam** or **ham** using a trained machine learning model. Built with scikit-learn, NLTK, and Streamlit — optimized for deployment on Streamlit Cloud.

---

## 🚀 Live Demo

👉 [Launch the App on Streamlit Cloud](https://message-spam-detector-3uo7thvcuq72wngzaavvat.streamlit.app/)

---

## 🧠 How It Works

- Preprocesses input text using:
  - Lowercasing
  - Regex-based tokenization
  - Stopword removal (`scikit-learn`)
  - Stemming (`PorterStemmer`)
- Transforms text using a saved `vectorizer.pkl`
- Predicts using a trained `model.pkl` (e.g., Naive Bayes or Logistic Regression)

---

## 📁 Project Structure

message-spam-detector/ 
|── app.py # Streamlit app
├── model.pkl # Trained ML model 
├── vectorizer.pkl # Text vectorizer (e.g., TF-IDF) 
├── requirements.txt # Python dependencies 
├── runtime.txt # Python version spec (3.10) 
├── .gitignore # Clean repo setup 
|── README.md # Project documentation


📦 Dependencies
streamlit
scikit-learn
nltk
re, string, pickle (built-in)

📌 Notes
No need for nltk.download() — uses PorterStemmer and scikit-learn stopwords for compatibility
Compatible with Python 3.10+ and Streamlit Cloud
Model and vectorizer are pre-trained and loaded via pickle

🙌 Credits
Built by Tejcodings
Inspired by real-world spam filtering use cases
