import re
import string
import numpy as np
import joblib
import nltk
from flask import Flask, request, render_template
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')


with open(r'vectorizer.pkl', 'rb') as f:
    vectorize = joblib.load(f)

with open(r'model.pkl', 'rb') as f:
    model = joblib.load(f)

app = Flask(__name__, static_url_path='/static')


def clean_data(text):
    text = text.lower()
    text = re.sub(r"<.*?>", " ", text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    lemmatizer = WordNetLemmatizer()
    a = []
    for w in text.split():
        if w not in stopwords.words('english'):
            if not w.isnumeric():
                a.append(lemmatizer.lemmatize(w))
    return " ".join(a)


@app.route('/review', methods=['POST', 'GET'])
def review():
    if request.method == 'POST':
        text = request.form['nm']
    else:
        text = request.args.get('nm')
    text = clean_data(text)
    text = [text]
    data = vectorize.transform(text).toarray()
    prediction = model.predict(data)
    return render_template('review.html', data=prediction)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)