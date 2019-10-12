def palperm(inp):
    chars = dict()
    for c in inp.lower():
        if c == ' ':
            continue

        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1

    odds = 0
    for val in chars.values():
        if val % 2 == 1:
            if odds > 0:
                return False

            odds += 1

    return True


def palperm2(inp):
    inp = sorted(inp.lower())
    print(inp)
    cnt = 0
    odds = 0
    curr = None
    for c in inp:
        if c == ' ':
            continue

        if curr is None:
            curr = c
            cnt = 1
            continue

        if c == curr:
            cnt += 1
        else:
            print(curr, cnt)
            if cnt % 2 == 1:
                if odds > 0:
                    return False

                odds += 1

            cnt = 1
            curr = c

    if cnt % 2 == 1 and odds > 0:
        return False

    return True


import pytest

@pytest.mark.parametrize("input,expected", [
    ("Tact Coa", True),
    ("Tact Coat", False),
    ("Tact Coa To", True),
    ("Tact Coa Tout", True),
    ("Tact Coa Tou1", False),
])
def test_palperm(input, expected):
    assert palperm(input) == expected
    assert palperm2(input) == expected

pytest.main()
