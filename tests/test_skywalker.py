import pytest
from app import skywalker, get_sentence

def test_get_sentence():
    assert get_sentence('Luke Skywalker', ['A New Hope', 'The Empire Strikes Back', 'Return of the Jedi', 'Revenge of the Sith']) == 'Luke Skywalker participated in A New Hope, The Empire Strikes Back, Return of the Jedi and Revenge of the Sith.'
    assert get_sentence('Anakin Skywalker', ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']) == 'Anakin Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith.'
    assert get_sentence('Shmi Skywalker', ['The Phantom Menace', 'Attack of the Clones', 'Revenge of the Sith']) == 'Shmi Skywalker participated in The Phantom Menace, Attack of the Clones and Revenge of the Sith.'

