from flask import Flask, render_template, request, jsonify
from grandpy_bot.parser import parse_search, MatchNotFound
from grandpy_bot.google_api import geocode
from grandpy_bot.media_api import wiki_api
from grandpy_bot.sentences import sentences_address, sentences_wiki
# import json
import os

app = Flask(__name__)


# Config options - Make sure you created a 'config.py' file.
# app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']


@app.route('/')
def index():
    API_KEY = os.getenv['GOOGLE_API_KEY']
    return render_template('index.html', key=API_KEY)


@app.route('/post_address', methods=['POST'])
def post_address():
    """Summary

    Returns:
        Json: returns json value
    """
    regex_request = None
    user_request = request.form["userText"]
    if user_request:
        try:
            regex_request = parse_search(user_request)
            print(regex_request)
        except MatchNotFound:
            return jsonify({"error": "Oospy... Veuillez recommencer!"})
        response = geocode(regex_request)
        response_wiki = wiki_api(response["lat"], response["lng"])
        random_sentences_address = sentences_address()
        random_sentences_wiki = sentences_wiki()
        response.update(response_wiki)
        response.update(random_sentences_address)
        response.update(random_sentences_wiki)
        print("reponse", response)
    else:
        return jsonify({"error": "Veuillez remplir le champ du formulaire..."})

    return jsonify(response)


if __name__ == "__main__":
    app.run()
