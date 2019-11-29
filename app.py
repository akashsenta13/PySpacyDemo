from flask import Flask, render_template, url_for, request
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/process', methods=["POST"])
def process():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        doc = nlp(rawtext)
        d = []
        for ent in doc.ents:
            text = ent.label_ + "   :   " + ent.text + \
                "   :   " + spacy.explain(ent.label_)
            d.append(text)

    results = d
    num_of_results = len(results)

    return render_template("index.html", results=results, num_of_results=num_of_results)


if __name__ == '__main__':
    app.run(debug=True)
