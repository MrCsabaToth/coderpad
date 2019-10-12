def is_all_unique_hash(text):
    """ TODO: Code doc """
    if not text:
        return False

    try:
        len(text)
    except TypeError:
        return False

    characters = dict()

    for character in text:
        if character in characters:
            return False

        characters[character] = True

    return True



def is_all_unique_in_place(text):
    """ TODO: Code doc """
    if not text:
        return False

    try:
        len(text)
    except TypeError:
        return False

    text = sorted(text)

    last = None
    for character in text:
        if last == character:
            return False

        last = character

    return True



import pytest


@pytest.mark.parametrize("input,expected", [
    (None, False),
    ('', False),
    (-1, False),
    ({}, False),
    ('aa', False),
    ('aba', False),
    ('abc', True),
])
def test_is_all_unique2(input, expected):
    assert is_all_unique_hash(input) == expected
    assert is_all_unique_in_place(input) == expected


from hypothesis import given
from hypothesis.strategies import text

@given(input=text())
def test_fuzz_is_all_unique(input):
    assert is_all_unique_hash(input) == is_all_unique_in_place(input)

pytest.main()
