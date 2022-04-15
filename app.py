import flask
import requests

app = flask.Flask(__name__)

def get_sentence(name, list_of_films):
    last_film_title = list_of_films.pop()
    return f'{name} participated in {", ".join(list_of_films)} and {last_film_title}.'

@app.route('/', methods=['GET'])
def index():
    return 'Go to /skywalker mf'

@app.route('/skywalker', methods=['GET'])
def skywalker():
    api_fetch = requests.get('https://swapi.dev/api/people/?search=skywalker')
    api_fetch_json = api_fetch.json()
    texts = []

    for i in api_fetch_json['results']:
        name = i['name']
        film_titles = []
        
        for j in i['films']:
            film = requests.get(j)
            film_json = film.json()
            film_title = film_json['title']
            film_titles.append(film_title)
        texts.append(get_sentence(name, film_titles))
        
    
    return flask.jsonify({'status': 200, 'description': ' '.join(texts)})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
