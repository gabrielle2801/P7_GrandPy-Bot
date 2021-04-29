from flask import Flask, render_template, request, jsonify
from grandpy_bot.parser import parse_search
from grandpy_bot.google_api import geocode
from grandpy_bot.media_api import wiki_api
import json

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
# app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/post_address', methods=['POST'])
def post_address():
    """Summary

    Returns:
        Json: returns json value
    """
    user_request = request.form["userText"]
    if user_request:
        regex_request = parse_search(user_request)
        response = geocode(regex_request)
        print(response)
        response_wiki = wiki_api(response["lat"], response["lng"])

        response.update(response_wiki)
        print(response)
    return jsonify(response)


if __name__ == "__main__":
    app.run()
