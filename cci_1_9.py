def rotated(s1, s2):
    concat = s2 + s2
    return s1 in concat

import pytest

@pytest.mark.parametrize("s1,s2,expected", [
    ("waterbottle", "", False),
    ("waterbottle", "waterbottle", True),
    ("waterbottle", "erbottlewat", True),
    ("waterbottle", "erbottlewta", False),
])
def test_rotated(s1, s2, expected):
    assert rotated(s1, s2) == expected

pytest.main()
