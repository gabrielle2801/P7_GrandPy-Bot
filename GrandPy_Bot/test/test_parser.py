import pytest
from grandpy_bot.parser import parse_search, MatchNotFound


def test_parser():
    cases = [
        ("adresse du pantheon ?", "pantheon"),
        ("Bonjour, saurais-tu où se trouve la librairie?", "librairie"),
        ("Hello, où pouvons-nous trouver une boulangerie?", "boulangerie"),
        ("Où se situe le garage Renault?", "garage Renault"),
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
