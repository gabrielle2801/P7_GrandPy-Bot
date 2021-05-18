import unittest
import os
import json

from grandpy_bot.views import app, post_address
from grandpy_bot import google_api


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
        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
        'lat': 48.8975156,
        'lng': 2.3833993,
        'extract': "Le quai de la Gironde est un quai situé le long du canal Saint-Denis, à Paris,"
        " dans le 19e arrondissement.\n\n\n== Situation et accès ==\nIl fait face au quai de la Charente,"
        "commence au quai de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce quai.",
        'sentences': 'Sans nul doute ... : ',
        'sentences_wiki': 'Il fut un temps où je venais flaner dans ce lieu ... : '}

    response = client.post('/post_address',
                           data={'userText': 'Ou se trouve OpenClassrooms ?'})

    # data = json.loads(response.get_data(as_text=True))
    # assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['lat'] == expected_response['lat']


def test_get_correct_coordinates(monkeypatch):
    coordinates = {

        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
        'lat': 48.8975156,
        'lng': 2.3833993,
    }

    class MockResponse:

        status_code = 200

        def json(self):
            return {
                "results": [
                    {
                        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
                        "geometry": {
                            "location": {
                                "lat": 48.8975156,
                                "lng": 2.3833993
                            }
                        }
                    }
                ]
            }

        def MockRequestsPost(url, params):
            return MockResponse()

        monkeypatch.setattr('requests.post', MockRequestsPost)
        result = post_address()
        assert result == coordinates
