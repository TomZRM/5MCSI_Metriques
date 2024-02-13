from flask import Flask, render_template, jsonify, request, session, redirect, url_for, flash
from datetime import datetime
from urllib.request import urlopen
import json
import sqlite3

app = Flask(__name__)

# Secret key nécessaire pour utiliser les sessions
app.secret_key = 'votre_clé_secrète_unique'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin':
            session['logged_in'] = True
            flash('Connexion réussie. Bienvenue !', 'success')
            return redirect(url_for('hello_world'))
        else:
            flash('Erreur de connexion. Veuillez réessayer.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Vous avez été déconnecté.', 'success')
    return redirect(url_for('hello_world'))

@app.route("/contact/")
def contact():
    if not session.get('logged_in'):
        flash('Veuillez vous connecter pour accéder à cette page.', 'warning')
        return redirect(url_for('login'))
    return render_template("contact.html")

@app.route('/tawarano/')
def meteo():
    # ... Votre code existant pour la route /tawarano/ ...

@app.route("/rapport/")
def rapport():
    # ... Votre code existant pour la route /rapport/ ...

@app.route("/histogramme/")
def histogramme():
    # ... Votre code existant pour la route /histogramme/ ...

@app.route("/commits/")
def commits():
    # ... Votre code existant pour la route /commits/ ...
  
if __name__ == "__main__":
    app.run(debug=True)
