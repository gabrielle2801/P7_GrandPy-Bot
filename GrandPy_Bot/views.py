from flask import Flask, render_template, request
from grandpy_bot.parser import parse_search
from grandpy_bot.google_api import geocode
from grandpy_bot.media_api import wiki_api

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
# app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/', methods=['POST', 'GET'])
def index():
    """Summary

    Returns:
        TYPE: Description
    """
    user_request = request.form.get('name')
    if user_request:
        regex_request = parse_search(user_request)
        response = geocode(regex_request)
        response_wiki = wiki_api(regex_request)
        # print(response_wiki_json)
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
