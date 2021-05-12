import unittest
import os
import json

from grandpy_bot.views import app


def test_index():
    # app = Flask(__name__)
    # API_KEY = os.getenv('GOOGLE_API_KEY_GEOCODE')
    # response = app.test_client().get('/')

    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200
    # assert response.template.name == 'index.html'


def test_post():
    client = app.test_client()

    expected_response = {
        'formatted_address': 'Champ de Mars, 5 Avenue Anatole France, 75007 Paris, France',
        'lat': 48.85837009999999,
        'lng': 2.2944813,
        'extract': 'La tour Eiffel  est une tour de fer puddlé de 324 mètres de hauteur (avec antennes) située à Paris, à l’extrémité nord-ouest du parc du Champ-de-Mars en bordure de la Seine dans le 7e arrondissement. Son adresse officielle est 5, avenue Anatole-France.\nConstruite en deux ans par Gustave Eiffel et ses collaborateurs pour l’Exposition universelle de Paris de 1889, et initialement nommée « tour de 300 mètres », elle est devenue le symbole de la capitale française et un site touristique de premier plan : il s’agit du troisième site culturel français payant le plus visité en 2015, avec 5,9 millions de visiteurs en 2016.',
        'sentences': 'Sans nul doute ... : ',
        'sentences_wiki': 'Il fut un temps où je venais flaner dans ce lieu ... : '}

    response = client.post('/post_address',
                           data={'userText': 'Ou se trouve la tour Eiffel?'})

    # data = json.loads(response.get_data(as_text=True))
    # assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['lat'] == expected_response['lat']
