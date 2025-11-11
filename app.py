import streamlit as st
import sys
import pickle
import re
import string
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from nltk.stem.porter import PorterStemmer
st.write("Python executable:", sys.executable)

ps = PorterStemmer()
stop_words = set(ENGLISH_STOP_WORDS)

def transform_text(text):
    text = text.lower()

    tokens = re.findall(r'\b\w+\b',text)

    filtered = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    stemmed = [ps.stem(i)for i in filtered]

    return " ".join(stemmed)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))


st.title("SMS/E-mail Spam Classifier")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):
    # 1 preprocess
    transformed_text = transform_text(input_sms)
    # 2.vectorize
    vectoriz_text = tfidf.transform([transformed_text])
    # 3.predict
    result = model.predict(vectoriz_text)
    # 4 display
    if result == 1:
        st.header("spam")
    else:
        st.header("Not a spam")




