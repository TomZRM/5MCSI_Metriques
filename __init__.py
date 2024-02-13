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

@app.route("/commits/")
def mescommits():
    # Effectuez une requête GET à l'API GitHub pour obtenir les données de commit
    commit_data = requests.get('https://api.github.com/repos/TomZRM/5MCSI_Metriques/commits').json()
    
    # Préparez les données pour le graphique
    commit_times = []  # Ceci va stocker nos données formatées pour le graphique

    for commit in commit_data:
        # Convertissez la date en un objet datetime, puis en une chaîne lisible
        date_str = commit['commit']['committer']['date']
        date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
        
        # Vous pouvez choisir de grouper par heure ou par jour, selon vos besoins
        commit_times.append([date_obj.strftime('%Y-%m-%d %H:%M'), 1])
    
    # Passez les données de commit au template
    return render_template("commits.html", commit_times=commit_times)

if __name__ == "__main__":
    app.run(debug=True)
