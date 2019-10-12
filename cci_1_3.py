def urlify(input):
    if not input:
        return input

    parts = input.strip().split(" ")
    return "%20".join(parts)


def urlify2(input):
    if not input:
        return input

    i = len(input) - 1
    j = i
    input = list(input)
    while j > 0:
        if input[j] == ' ':
            j -= 1
        else:
            break

    while j >= 0 and i >= 0:
        print(i, j, input)
        if input[j] != ' ':
            input[i] = input[j]
            i -= 1
            j -= 1
        else:
            j -= 1
            input[i] = '0'
            i -= 1
            input[i] = '2'
            i -= 1
            input[i] = '%'
            i -= 1

    return ''.join(input)


import pytest

@pytest.mark.parametrize("input,expected", [
    ('', ''),
    ('   ', ''),
    ('Mr John Smith    ', 'Mr%20John%20Smith'),
])
def test_urlify(input, expected):
    assert urlify(input) == expected


@pytest.mark.parametrize("input,expected", [
    ('', ''),
    ('Mr John Smith    ', 'Mr%20John%20Smith'),
])
def test_urlify2(input, expected):
    assert urlify2(input) == expected


pytest.main()
