import requests


def wiki_api(request_wiki):
    """Summary

    Args:
        request_wiki (TYPE): Description

    Returns:
        TYPE: Description
    """
    url_wiki = "https://fr.wikipedia.org/w/api.php?"
    # params = "action=query&prop=revisions&rvprop=content&rvsection=0&format=json&titles="
    params = "action=query&prop=extracts&exsentences=10&exlimit=1&explaintext=1&format=json&titles="
    wiki_request = url_wiki + params + request_wiki
    response_wiki = requests.get(wiki_request)
    response_wiki_json = response_wiki.json()
    query = response_wiki_json["query"]["pages"]
    page_id = list(query.keys())[0]
    print(wiki_request)
    print(response_wiki)
    extract = query[page_id]["extract"]
    print(extract)
    return extract
