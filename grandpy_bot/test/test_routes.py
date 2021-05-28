import json
import requests

from grandpy_bot.views import app


def test_index():

    client = app.test_client()
    url = '/'

    response = client.get(url)
    assert response.status_code == 200


def test_get_correct_post(monkeypatch):
    expected_response = {
        'formatted_address': 'test google',
        'lat': 48.8975156,
        'lng': 2.3833993,
        'extract': "test wiki",
        'sentences': 'Sans nul doute ... : ',
        'sentences_wiki': 'Il fut un temps où je venais flaner dans ce lieu ... : '}

    class MockResponseGoogle():

        status_code = 200

        def json(self):
            return {
                "results": [
                    {
                        'formatted_address': 'test google',
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
                          "extract": "test wiki"},
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

    monkeypatch.setattr(requests, "get", MockRequestsPost)
    client = app.test_client()
    response = client.post('/post_address',
                           data={'userText': 'Ou se trouve OpenClassrooms ?'})
    response_data = json.loads(response.data)
    # print(response_data)
    assert response_data['extract'] == expected_response['extract']
    assert response_data['formatted_address'] == expected_response['formatted_address']
    assert response_data['lat'] == expected_response['lat']
