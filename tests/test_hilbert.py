"""
    Testing for sfcpy.hilbert
"""

import pytest

from sfcpy.hilbert import read_hc_tape, get_hc_tape, prepare_image, tape_reader
from sfcpy.hilbert import left, down, right, up
from sfcpy.data import data


HC_TABLE = "sfcpy/hc_lookup.txt"


# test read_hc_tape
def test_read_hc_tape():
    assert read_hc_tape(HC_TABLE, 2) == "odrurrdldrdlluld"
    assert read_hc_tape(HC_TABLE, 3) == "odrurrdldrdllulddrdlddrurdruulurrrdlddrurdruuluruuldllurulurrdru"
    assert read_hc_tape(HC_TABLE, 4) == "odrurrdldrdllulddrdlddrurdruulurrrdlddrurdruuluruuldllurulurrdrur\
rdlddrurdruulurrdrurrdldrdlluldddrurrdldrdlluldlluruuldlulddrdldrdlddrurdruulurrdrurrdldrdlluldddrurrd\
ldrdlluldlluruuldlulddrdlluldllurulurrdruuluruuldlulddrdllluruuldlulddrdlddrurrdldrdlluld"


# test get_hc_tape
def test_get_hc_tape():
    assert get_hc_tape(2) == "odrurrdldrdlluld"
    assert get_hc_tape(3) == "odrurrdldrdllulddrdlddrurdruulurrrdlddrurdruuluruuldllurulurrdru"
    assert get_hc_tape(4) == "odrurrdldrdllulddrdlddrurdruulurrrdlddrurdruuluruuldllurulurrdrur\
rdlddrurdruulurrdrurrdldrdlluldddrurrdldrdlluldlluruuldlulddrdldrdlddrurdruulurrdrurrdldrdlluldddrurrd\
ldrdlluldlluruuldlulddrdlluldllurulurrdruuluruuldlulddrdllluruuldlulddrdlddrurrdldrdlluld"


# test moving
PTS = (0, 0)

# test left
def test_left():
    assert left(PTS) == (-1, 0)


# test down 
def test_down():
    assert down(PTS) == (0, 1)


# test right 
def test_right():
    assert right(PTS) == (1, 0)


# test up 
def test_up():
    assert up(PTS) == (0, -1)


# test tape_reader
def test_tape_reader():
    assert tape_reader['l'](PTS) == (-1, 0)
    assert tape_reader['d'](PTS) == (0, 1)
    assert tape_reader['r'](PTS) == (1, 0)
    assert tape_reader['u'](PTS) == (0, -1)