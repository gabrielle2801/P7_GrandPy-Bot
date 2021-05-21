from grandpy_bot import media_api


def test_get_returns_correct_extract(monkeypatch):
    extract = {'extract':
               "Le quai de la Gironde est un quai situé le long du canal Saint-Denis, à Paris,"
               " dans le 19e arrondissement.\n\n\n== Situation et accès ==\nIl fait face au quai de la Charente,"
               "commence au quai de l'Oise et se termine avenue Corentin-Cariou.\nLa ligne \u2009 du tramway passe sur ce quai."
               }

    class MockResponse:

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

    def MockRequestsGet(url, params):

        return MockResponse()

    monkeypatch.setattr('requests.get', MockRequestsGet)
    result = media_api.wiki_api(48.8975156, 2.3833993)
    assert result == extract
