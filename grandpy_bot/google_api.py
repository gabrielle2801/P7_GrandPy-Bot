import requests
import urllib.request
import os


class AddressNotFound(Exception):
    pass


def geocode(address):
    """Call geocoding google map api

    Args:
        address (STRING): user input

    Returns:
        dictionary: returns values (address, coordinates)
    """
    API_KEY = os.getenv('GOOGLE_API_KEY')

    # urllib.parse.urlencode : transforms url string into its component
    params = urllib.parse.urlencode({
        "address": address,
        "key": API_KEY,
        "region": "fr"
    })

    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json?", params=params)
    if response.status_code == 200:
        try:
            result = response.json()['results']
            return {
                "formatted_address": result[0]['formatted_address'],
                "lat": result[0]['geometry']['location']["lat"],
                "lng": result[0]['geometry']['location']["lng"],
            }
        except IndexError:
            raise AddressNotFound(
                "Oospy demande incorrect, reformulez votre demande")
