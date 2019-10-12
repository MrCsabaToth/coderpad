def zero1(m):
    h = len(m)
    w = len(m[0])
    cols = [False] * w
    rows = [False] * h
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(h):
        for j in range(w):
            if rows[i] or cols[j]:
                m[i][j] = 0

def zero2(m):
    h = len(m)
    w = len(m[0])
    cols = [False] * w
    rows = [False] * h
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                rows[i] = True
                cols[j] = True

    for i in range(h):
        if rows[i]:
            m[i] = [0] * w

    for i in range(h):
        for j in range(w):
            if cols[j]:
                m[i][j] = 0

def zero3(m):
    h = len(m)
    w = len(m[0])

    zero0row = any(el == 0 for el in m[0])
    zero0col = any(m[i][0] == 0 for i in range(h))
    for i in range(h):
        for j in range(w):
            if m[i][j] == 0:
                m[i][0] = 0
                m[0][j] = 0

    for i in range(1, h):
        if m[i][0] == 0:
            m[i] = [0] * w

    for j in range(1, w):
        if m[0][j] == 0:
            for i in range(h):
                m[i][j] = 0

    if zero0row:
        m[0] = [0] * w

    if zero0col:
        for i in range(h):
            m[i][0] = 0

import pytest
import copy

@pytest.mark.parametrize("matrix,expected", [
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]],
     [[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]]),
    ([[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]],
     [[1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]]),
    ([[0, 1, 1],
      [1, 1, 1],
      [1, 1, 1]],
     [[0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]]),
    ([[1, 1, 0],
      [1, 1, 1],
      [1, 1, 1]],
     [[0, 0, 0],
      [1, 1, 0],
      [1, 1, 0]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 0]],
     [[1, 1, 0],
      [1, 1, 0],
      [0, 0, 0]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [0, 1, 1]],
     [[0, 1, 1],
      [0, 1, 1],
      [0, 0, 0]]),

    ([[1, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     [[1, 0, 1, 1],
      [0, 0, 0, 0],
      [1, 0, 1, 1],
      [1, 0, 1, 1]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 1]],
     [[1, 1, 0, 1],
      [1, 1, 0, 1],
      [0, 0, 0, 0],
      [1, 1, 0, 1]]),
    ([[0, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     [[0, 0, 0, 0],
      [0, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1]]),
    ([[1, 1, 1, 0],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     [[0, 0, 0, 0],
      [1, 1, 1, 0],
      [1, 1, 1, 0],
      [1, 1, 1, 0]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 0]],
     [[1, 1, 1, 0],
      [1, 1, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1]],
     [[0, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 0, 0, 0]]),

    ([[1, 1, 1, 1],
      [1, 0, 1, 1],
      [1, 1, 1, 1]],
     [[1, 0, 1, 1],
      [0, 0, 0, 0],
      [1, 0, 1, 1]]),
    ([[1, 1, 1, 1],
      [1, 1, 0, 1],
      [1, 1, 1, 1]],
     [[1, 1, 0, 1],
      [0, 0, 0, 0],
      [1, 1, 0, 1]]),
    ([[0, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     [[0, 0, 0, 0],
      [0, 1, 1, 1],
      [0, 1, 1, 1]]),
    ([[1, 1, 1, 0],
      [1, 1, 1, 1],
      [1, 1, 1, 1]],
     [[0, 0, 0, 0],
      [1, 1, 1, 0],
      [1, 1, 1, 0]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [1, 1, 1, 0]],
     [[1, 1, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0]]),
    ([[1, 1, 1, 1],
      [1, 1, 1, 1],
      [0, 1, 1, 1]],
     [[0, 1, 1, 1],
      [0, 1, 1, 1],
      [0, 0, 0, 0]]),


    ([[1, 1, 1],
      [1, 0, 1],
      [1, 1, 1],
      [1, 1, 1]],
     [[1, 0, 1],
      [0, 0, 0],
      [1, 0, 1],
      [1, 0, 1]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 0],
      [1, 1, 1]],
     [[1, 0, 1],
      [1, 0, 1],
      [0, 0, 0],
      [1, 0, 1]]),
    ([[0, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]],
     [[0, 0, 0],
      [0, 1, 1],
      [0, 1, 1],
      [0, 1, 1]]),
    ([[1, 1, 0],
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1]],
     [[0, 0, 0],
      [1, 1, 0],
      [1, 1, 0],
      [1, 1, 0]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 0]],
     [[1, 1, 0],
      [1, 1, 0],
      [1, 1, 0],
      [0, 0, 0]]),
    ([[1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
      [0, 1, 1]],
     [[0, 1, 1],
      [0, 1, 1],
      [0, 1, 1],
      [0, 0, 0]]),
])
def test_zero(matrix, expected):
    m = copy.deepcopy(matrix)
    zero1(m)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] == expected[i][j]

    m = copy.deepcopy(matrix)
    zero2(m)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] == expected[i][j]

    m = copy.deepcopy(matrix)
    zero3(m)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] == expected[i][j]

pytest.main()
