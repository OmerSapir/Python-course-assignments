import counter
import pytest


text = 'business_logic.txt'

@pytest.mark.parametrize("ch, expected", [(text, 418)])
def test_characters(ch, expected):
    result = counter.count_characters(ch)
    assert (result == expected)

@pytest.mark.parametrize("ln, expected", [(text, 5)])
def test_lines(ln, expected):
    result = counter.count_lines(ln)
    assert (result == expected)

@pytest.mark.parametrize("w, expected", [(text, 65)])
def test_words(w, expected):
    result = counter.count_words(w)
    assert (result == expected)


