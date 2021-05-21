import requests


def wiki_api(lat, lng):
    """Call wikipedia api


    Args:
        lat (FLOAT): latitude extract from user input
        lng (FLOAT): longitude extract from user input

    Returns:
        dictionary: extract from wikipedia api
        first paragraph of the wikipedia page
    """
    coord = str(lat) + "|" + str(lng)
    print(coord)

    params = {
        "action": "query",
        "prop": "extracts",
        "generator": "geosearch",
        "exsentences": "3",
        "exlimit": "1",
        "explaintext": "True",
        "ggsradius": "200",
        "ggscoord": coord,
        "ggslimit": "3",
        "format": "json",

    }

    response_wiki = requests.get("https://fr.wikipedia.org/w/api.php?",
                                 params=params)
    if response_wiki.status_code == 200:
        try:
            wiki = response_wiki.json()["query"]["pages"]
            page_id = list(wiki.keys())[0]
            extract = wiki[page_id]["extract"]
            return {"extract": extract}

        except KeyError:
            return {"extract": "Tiens, cette contrée m'est inconnue ..."}