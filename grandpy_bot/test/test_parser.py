import pytest
from grandpy_bot.parser import parse_search, MatchNotFound


def test_parser():
    cases = [
        ("Bonjour, saurais-tu où se trouve la librairie?", "librairie"),
        ("Hello, où pouvons-nous trouver une boulangerie?", "une boulangerie"),
        ("Où se situe le garage Renault?", "garage Renault"),
        ("Pourrais tu me donner l'adresse d'OpenClassrooms?", "OpenClassrooms"),
        ("Où se situent les jardins du Luxembourg?", "les jardins du Luxembourg"),
        ("Donne moi l'adresse du Panthéon?", "Panthéon"),
        ("Bonjour, saurais-tu où se trouve le musée d'Orsay?", "musée d'Orsay"),
        ("Hello, où pouvons-nous trouver un magasin de sport?", "un magasin de sport"),
    ]

    for case, expected in cases:
        assert parse_search(case) == expected


def test_parser_not_match():
    cases = [
        "Quelle heure est-il ?", "Bonjour, je veux aller à Paris"
    ]
    for case in cases:
        with pytest.raises(MatchNotFound):
            assert parse_search(case)
