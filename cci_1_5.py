def oneedit(a, b):
    if a == b:
        return True

    lena = len(a)
    lenb = len(b)
    if abs(lena - lenb) > 1:
        return False

    if lena == lenb:
        cnt = 0
        for i in range(lena):
            if a[i] != b[i]:
                cnt += 1
                if cnt > 1:
                    return False
        
        return True

    cnt = 0
    ai = 0
    bi = 0
    while bi < lenb and ai < lena:
        if a[ai] != b[bi]:
            if cnt > 0:
                return False

            if lena > lenb:
                ai += 1
            else:
                bi += 1

            cnt += 1
        else:
            ai += 1
            bi += 1

    return cnt == 0 and (ai != lena or bi != lenb) or ai == lena and bi == lenb and cnt <= 1


def oneedit2(a, b):
    if a == b:
        return True

    lena = len(a)
    lenb = len(b)
    if abs(lena - lenb) > 1:
        return False

    cnt = 0
    ai = 0
    bi = 0
    while bi < lenb and ai < lena:
        if a[ai] != b[bi]:
            if cnt > 0:
                return False

            if lena > lenb:
                ai += 1
            elif lena < lenb:
                bi += 1
            else:
                ai += 1
                bi += 1

            cnt += 1
        else:
            ai += 1
            bi += 1

    return cnt == 0 and (ai != lena or bi != lenb) or ai == lena and bi == lenb and cnt <= 1


import pytest

@pytest.mark.parametrize("a,b,expected", [
    (None, None, True),
    ('', '', True),
    ('a', 'b', True),
    ('aa', 'ab', True),
    ('aa', 'bb', False),
    ('aa', 'aaaa', False),
    ('pale', 'ple', True),
    ('pales', 'pale', True),
    ('pale', 'bale', True),
    ('pale', 'bake', False),
    ('pale', 'pake', True),
    ('ale', 'pale', True),
    ('pale', 'ale', True),
    ('pale', 'pales', True),
    ('pale', 'palb', True),
])
def test_oneedit(a, b, expected):
    assert oneedit(a, b) == expected
    assert oneedit2(a, b) == expected

pytest.main()
