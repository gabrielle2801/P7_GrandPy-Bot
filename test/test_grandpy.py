from GrandPy_Bot.views import app
import pytest
import GrandPy_Bot.views as script


def hello(name):
    return 'Hello ' + name


def test_hello():
    assert hello('Celine') == 'Hello Celine'


class Test_interface:
    def test_home_page_header(self):
        tester = app.test_client()
        response = tester.get("/")

        assert response.status_code == 200
        html = response.get_data(as_text=True)


class Test_parser:

    def test_parser(self):
        user_request = "bonjour grandpy_bot! Où se trouve le Musée d'Orsay ?"
        assert script.regex(user_request) == "Musée+Orsay"
