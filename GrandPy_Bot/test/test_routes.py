import json
import requests

from grandpy_bot.views import app


def test_index():

    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


# def test_post():
#     client = app.test_client()

#     expected_response = {
#         'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
#         'lat': 48.8975156,
#         'lng': 2.3833993,
#         'extract': "Le quai de la Gironde est un quai situé le long du canal Saint-Denis, à Paris,"
#         " dans le 19e arrondissement.\n\n\n== Situation et accès ==\nIl fait face au quai de la Charente,"
#         "commence au quai de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce quai.",
#         'sentences': 'Sans nul doute ... : ',
#         'sentences_wiki': 'Il fut un temps où je venais flaner dans ce lieu ... : '}

#     response = client.post('/post_address',
#                            data={'userText': 'Ou se trouve OpenClassrooms ?'})

#
#     response_data = json.loads(response.data)
#     assert response_data['lat'] == expected_response['lat']


def test_get_correct_post(monkeypatch):
    expected_response = {
        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
        'lat': 48.8975156,
        'lng': 2.3833993,
        'extract': "Le quai de la Gironde est un quai situé le long du canal Saint-Denis, à Paris,"
        " dans le 19e arrondissement.\n\n\n== Situation et accès ==\nIl fait face au quai de la Charente,"
        "commence au quai de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce quai.",
        'sentences': 'Sans nul doute ... : ',
        'sentences_wiki': 'Il fut un temps où je venais flaner dans ce lieu ... : '}

    class MockResponseGoogle():

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

    class MockResponseWiki():
        status_code = 200

        def json(self):
            return {"continue":
                    {"excontinue": 1, "continue": "||"},
                    "query":
                    {"pages":
                        {"3120649":
                         {"pageid": 3120649, "ns": 0,
                          "title": "Quai de la Gironde",
                          "index": -1,
                          "extract": "Le quai de la Gironde est un quai situ\u00e9 le long du canal Saint-Denis,"
                          " \u00e0 Paris, dans le 19e arrondissement.\n\n\n== Situation et acc\u00e8s ==\nIl fait face au quai de la Charente,"
                          "commence au quai de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce quai."},
                         "3124793":
                         {"pageid": 3124793, "ns": 0,
                             "title": "Square du Quai-de-la-Gironde", "index": 0},
                            "11988883": {"pageid": 11988883, "ns": 0, "title": "Parc du Pont de Flandre", "index": 1}
                         }
                     }
                    }

    def MockRequestsPost(url, params):
        if url.startswith("https://maps.googleapis.com/maps/api/geocode/json?"):
            return MockResponseGoogle()
        else:
            return MockResponseWiki()

    monkeypatch.setattr(requests, "post", MockRequestsPost)
    client = app.test_client()
    response = client.post('/post_address',
                           data={'userText': 'Ou se trouve OpenClassrooms ?'})
    response_data = json.loads(response.data)
    assert (response_data['formatted_address'], response_data['lat']) == (
        expected_response['formatted_address'], expected_response['lat'])
