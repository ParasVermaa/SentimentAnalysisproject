from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

sent_pipeline = pipeline("sentiment-analysis")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    result = sent_pipeline(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
