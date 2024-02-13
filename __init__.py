from flask import Flask, render_template, jsonify
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/tawarano/')
def tawarano():
    # Remplacez 'xxx' par votre clé API réelle pour OpenWeatherMap si vous en avez une.
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion de Kelvin en °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)
    
@app.route('/rapport/')
def rapport():
    # Cette fonction va rendre la page 'graphique.html' du dossier 'templates'.
    return render_template('graphique.html')

@app.route('/histogramme/')
def histogramme():
    # Rendre la page histogramme.html lorsque la route /histogramme/ est accédée
    return render_template('histogramme.html')

@app.route('/contact/')
def contact():
    return render_template('contact.html')

from flask import Flask, render_template, jsonify
import requests
from datetime import datetime

app = Flask(__name__)

# ... vos autres routes ...

@app.route('/commits/')
def commits():
    commit_data = requests.get('https://github.com/TomZRM/5MCSI_Metriques/blob/main/templates/commits.html').json()
    commit_times = []

    for commit in commit_data:
        commit_time = commit['commit']['author']['date']
        date_object = datetime.strptime(commit_time, '%Y-%m-%dT%H:%M:%SZ')
        commit_times.append({'date': date_object.strftime('%Y-%m-%d %H:%M'), 'minute': date_object.minute})

    return render_template('commits.html', commit_times=commit_times)

if __name__ == "__main__":
    app.run(debug=True)
