from flask import Flask, render_template, request
import re
import requests

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/', methods=['POST', 'GET'])
def index():
    """Summary

    Returns:
        TYPE: Description
    """
    user_request = request.form.get('name')
    if user_request:
        regex_request = regex(user_request)
        print(regex_request)
        response = geocode(regex_request)
        response_wiki = wiki_api(regex_request)
        print(response_wiki)
        print("salut")
        response_json = response.json()
        response_wiki_json = response_wiki.json()
        query = response_wiki_json["query"]
        # print(query)
        # print(query.get("extract"))
        print(response_json)
        lat = response_json.get("results")

        #lat1 = lat.get("0")
        #lat2 = lat1.get("geometry")
        #lat3 = lat2.get("location")

        coordonnees = [data.get('location') for data in lat]
        print(coordonnees)
        # print(response_wiki_json)
    return render_template('index.html')


def geocode(result_regex):
    """Summary

    Args:
        result_regex (TYPE): Description

    Returns:
        TYPE: Description
    """
    url_geocode = "https://maps.googleapis.com/maps/api/geocode/json?address="

    print(url_geocode + result_regex
          + "&key=AIzaSyCAl-yv3W7f05VpqqCm-Ka_zE_hzyzVRfw")
    response = requests.get(url_geocode + result_regex
                            + "&key=AIzaSyCAl-yv3W7f05VpqqCm-Ka_zE_hzyzVRfw")
    print(response)
    return response


def regex(user_request):
    """Summary

    Parameters:
        user_request (TYPE): Description

    Returns:
        TYPE: Description
    """
    result = re.findall(r"[A-Z][a-z]\w+", user_request)
    result_regex = '+'.join(result)
    return result_regex


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

    print(wiki_request)
    print(response_wiki)
    return response_wiki


if __name__ == "__main__":
    app.run()
