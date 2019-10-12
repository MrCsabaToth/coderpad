def hist(text):
    hst = dict()

    for ch in text:
        if ch not in hst:
            hst[ch] = 1
        else:
            hst[ch] += 1
    
    return hst


def is_perm(a, b):
    if not a or not b:
        return False

    if len(a) != len(b):
        return False

    a_hist = hist(a)
    b_hist = hist(b)

    for (ha, count) in a_hist.items():
        if ha not in b_hist or b_hist[ha] != count:
            return False

    return True


def is_perm_range(a, b):
    if not a or not b:
        return False

    if len(a) != len(b):
        return False

    a = sorted(a)
    b = sorted(b)

    for i in range(len(a)):
        if a[i] != b[i]:
            return False

    return True



def is_perm_zip(a, b):
    if not a or not b:
        return False

    if len(a) != len(b):
        return False

    a = sorted(a)
    b = sorted(b)

    for (ac, bc) in zip(a, b):
        if ac != bc:
            return False

    return True


def is_perm_3(a, b):
    if not a or not b:
        return False

    if len(a) != len(b):
        return False

    a = sorted(a)
    b = sorted(b)

    return a == b


import pytest


@pytest.mark.parametrize("a,b,expected", [
    (None, 'b', False),
    ('', 'b', False),
    ('a', None, False),
    ('a', '', False),
    ('abc', 'cde', False),
    ('aba', 'bab', False),
    ('abc', 'abc', True),
    ('abc', 'cba', True),
    ('abc', 'bca', True),
    ('abraka', 'karaba', True),
])
def test_is_all_unique(a, b, expected):
    assert is_perm(a, b) == expected
    assert is_perm_range(a, b) == expected
    assert is_perm_zip(a, b) == expected
    assert is_perm_3(a, b) == expected


pytest.main()
