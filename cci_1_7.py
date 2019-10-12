def rotate_m(m):
    if not m:
        return m

    n = len(m)
    if len(m[0]) != n:
        return None

    print(m)
    for i in range((n + 1) // 2):
        for j in range(i, n - i - 1):
            tmp = m[j][n - i - 1]
            m[j][n - i - 1] = m[i][j]
            tmp2 = m[n - i - 1][n - j - 1]
            m[n - i - 1][n - j - 1] = tmp
            tmp = m[n - j - 1][i]
            m[n - j - 1][i] = tmp2
            m[i][j] = tmp

import pytest

@pytest.mark.parametrize("n,matrix,expected", [
    (2,
     [[0, 1],
      [2, 3]],
     [[2, 0],
      [3, 1]],
    ),
    (3,
     [[0, 1, 2],
      [3, 4, 5],
      [6, 7, 8]],
     [[6, 3, 0],
      [7, 4, 1],
      [8, 5, 2]]),
    (4,
     [[0, 1, 2, 3],
      [4, 5, 6, 7],
      [8, 9, 10, 11],
      [12, 13, 14, 15]],
     [[12, 8, 4, 0],
      [13, 9, 5, 1],
      [14, 10, 6, 2],
      [15, 11, 7, 3]]),
    (5,
     [[0, 1, 2, 3, 4],
      [5, 6, 7, 8, 9],
      [10, 11, 12, 13, 14],
      [15, 16, 17, 18, 19],
      [20, 21, 22, 23, 24]],
     [[20, 15, 10, 5, 0],
      [21, 16, 11, 6, 1],
      [22, 17, 12, 7, 2],
      [23, 18, 13, 8, 3],
      [24, 19, 14, 9, 4]]),
])
def test_rotate_m(n, matrix, expected):
    matrix = list()
    for i in range(n):
        matrix.append(list(range(i * n, (i + 1) * n)))

    rotate_m(matrix)
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(i, j)
            assert matrix[i][j] == expected[i][j]

pytest.main()
