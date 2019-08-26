from collections import namedtuple
import pytest

playlist=namedtuple('Playlist',['song', 'artist','stop', 'id' ])
playlist.__new__.__defaults__ = (None,False,None, None )

def test_asdict():
    """asdict should return as a dictionary"""
    t_list = playlist("Hojo Clan", "Shikken Hanzo", True,25)
    t_dict = t_list._asdict()
    expected = {
        "song": "Hojo Clan",
        "artist": "Shikken Hanzo",
        "stop": True,
        "id" : 25
    }
    assert "Samurai" in t_list.song


def test_entries():
    """test the entries in the tuple"""
    t_list = playlist("Webaba", "Culoe de Song", True, 21)
    assert t_list.song == "Webaba"