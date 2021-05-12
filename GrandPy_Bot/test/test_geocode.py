from grandpy_bot import google_api


def test_get_returns_correct_coordinates(monkeypatch):
    coordinates = {

        'formatted_address': '10 Quai de la Charente, 75019 Paris, France',
        'lat': 48.8975156,
        'lng': 2.3833993
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

    def MockRequestsGet(url, params):

        return MockResponse()

    monkeypatch.setattr('requests.get', MockRequestsGet)
    result = google_api.geocode('OpenClassrooms')
    assert result == coordinates
