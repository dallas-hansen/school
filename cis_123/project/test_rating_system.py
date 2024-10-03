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
    assert add_rating(movies_ratings) == {'Inception': 9.0, 
                                          'The Dark Knight': 9.1, 
                                          'Interstellar': 8.6, 
                                          'The Matrix': 8.7, 
                                          'Parasite': 8.6, 
                                          'Forrest Gump': 8.8, 
                                          'The Godfather': 9.2, 
                                          'Pulp Fiction': 8.9, 
                                          'Deadpool': 10.0}

def test_remove_rating(monkeypatch):
    inputs = iter("Deadpool")
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert remove_rating(movies_ratings) == {'Inception': 9.0,
                                             'The Dark Knight': 9.1, 
                                             'Interstellar': 8.6, 
                                             'The Matrix': 8.7, 
                                             'Parasite': 8.6, 
                                             'Forrest Gump': 8.8, 
                                             'The Godfather': 9.2, 
                                             'Pulp Fiction': 8.9, 
                                             'Deadpool': 10.0}
# def test_display_ratings(capsys):
#     display_ratings(movies_ratings)
#     captured = capsys.readouterr()
#     assert captured.out == """The movie: Inception is rated: 9.0
# The movie: The Dark Knight is rated: 9.1
# The movie: Interstellar is rated: 8.6
# The movie: The Matrix is rated: 8.7
# The movie: Parasite is rated: 8.6
# The movie: Forrest Gump is rated: 8.8
# The movie: The Godfather is rated: 9.2
# The movie: Pulp Fiction is rated: 8.9"""