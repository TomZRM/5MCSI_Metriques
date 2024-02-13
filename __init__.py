from flask import Flask, render_template, jsonify
from datetime import datetime
from urllib.request import urlopen
import json
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Assurez-vous que le fichier hello.html est dans le dossier "templates".

@app.route('/contact/')
def contact():
    return "<h2>Ma page de contact</h2>"  # Cette ligne répondra avec un simple message HTML.

if __name__ == "__main__":
    app.run(debug=True)
