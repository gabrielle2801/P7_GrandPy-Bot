import requests


def geocode(result_regex):
    """Summary

    Args:
        result_regex (TYPE): Description

    Returns:
        TYPE: Description
    """
    url_geocode = "https://maps.googleapis.com/maps/api/geocode/json?address="
    response = requests.get(url_geocode + result_regex
                            + "&key=AIzaSyCAl-yv3W7f05VpqqCm-Ka_zE_hzyzVRfw")
    response_json = response.json()

    results = response_json.get("results")

    coordonnees = results[0]["geometry"]["location"]
    lat = coordonnees["lat"]
    lng = coordonnees["lng"]
    #print("latitude&longitude", lat1)
    print(lat, lng)
    return lat, lng
