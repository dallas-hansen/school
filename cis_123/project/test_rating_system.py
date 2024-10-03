from rating_system import *
import unittest

movies_ratings = {
    "Inception": 9.0,
    "The Dark Knight": 9.1,
    "Interstellar": 8.6,
    "The Matrix": 8.7,
    "Parasite": 8.6,
    "Forrest Gump": 8.8,
    "The Godfather": 9.2,
    "Pulp Fiction": 8.9
}

def test_add_rating(monkeypatch):
    inputs = iter(["Deadpool", "10"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert add_rating(movies_ratings) == {'Inception': 9.0, 'The Dark Knight': 9.1, 'Interstellar': 8.6, 'The Matrix': 8.7, 'Parasite': 8.6, 'Forrest Gump': 8.8, 'The Godfather': 9.2, 'Pulp Fiction': 8.9, 'Deadpool': 10.0}

# def test_remove_rating(movies_ratings):
#     remove_rating(movies_ratings)
#     assert(movies_ratings['Inception'], 8.7)

# def test_display_ratings(self):
#     display_ratings(movies_ratings)
#     assert(movies_ratings['Inception'], 8.7)
