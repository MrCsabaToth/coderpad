def strcmp(s):
    t = ""
    if not s:
        return s

    last = s[0]
    cnt = 1
    for c in s[1:]:
        if c != last:
            t += "{}{}".format(last, cnt)
            cnt = 1
            last = c
            if len(t) > len(s):
                return s
        else:
            cnt += 1

    t += "{}{}".format(last, cnt)
    if len(t) > len(s):
        return s

    return t


import pytest

@pytest.mark.parametrize("s,expected", [
    (None, None),
    ('', ''),
    ('a', 'a'),
    ('aa', 'a2'),
    ('aaa', 'a3'),
    ('aabcccccaaa', 'a2b1c5a3'),
    ('abc', 'abc'),
])
def test_oneedit(s, expected):
    assert strcmp(s) == expected

pytest.main()
