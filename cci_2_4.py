class Node(object):
    next = None
    data = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        n = self
        ret = "[{}".format(n.data)
        while n.next != None:
            n = n.next
            ret += ", {}".format(n.data)

        ret += "]"
        return ret

    def append(self, data):
        end = Node(data)
        n = self
        while n.next != None:
            n = n.next

        n.next = end

    def array(self):
        n = self
        lst = [n.data]
        while n.next != None:
            n = n.next
            lst.append(n.data)

        return lst

    def get(self, i):
        j = 0
        ll = self
        while j < i and ll:
            ll = ll.next
            j += 1

        return ll


def partition1(ll, data):
    head = None
    right = None
    left = None
    prev = None
    while ll:
        if ll.data < data:
            if not left:
                left = ll
                head = ll
            else:
                left.next = ll
                left = left.next

            if prev:
                prev.next = ll.next
        else:
            if not right:
                right = ll
            prev = ll

        ll = ll.next

    if head:
        left.next = right
        return head

    return right
        


def build(lst):
    head = None
    prev = None
    for item in lst:
        n = Node(item)
        if prev:
            prev.next = n
        else:
            head = n

        prev = n

    return head


import pytest


@pytest.mark.parametrize("array", [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_get(array):
    n = len(array)
    ll = build(array)

    for i in range(n):
        print(i)
        assert ll.get(i).data == array[i]


@pytest.mark.parametrize("array", [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_build(array):
    assert build(array).array() == array


@pytest.mark.parametrize("array,item,expected", [
    ([3, 5, 8, 5, 10, 2, 1], 5, [3, 2, 1, 5, 8, 5, 10]),
    ([7, 2, 3, 9, 10, 1, 9, 8, 4, 8], 5, [2, 3, 1, 4, 7, 9, 10, 9, 8, 8]),
    ([2, 3, 9, 5, 9, 1, 7, 5, 5, 4], 5, [2, 3, 1, 4, 9, 5, 9, 7, 5, 5]),
    ([3, 6, 4, 5, 3, 6, 10, 4, 7, 9], 5, [3, 4, 3, 4, 6, 5, 6, 10, 7, 9]),
    ([3, 6, 4, 5, 3, 6, 10, 4, 7, 9], 0, [3, 6, 4, 5, 3, 6, 10, 4, 7, 9]),
    ([3, 6, 4, 5, 3, 6, 10, 4, 7, 9], 1, [3, 6, 4, 5, 3, 6, 10, 4, 7, 9]),
    ([3, 6, 4, 5, 3, 6, 10, 4, 7, 9], 2, [3, 6, 4, 5, 3, 6, 10, 4, 7, 9]),
])
def test_partition(array, item, expected):
    ll = build(array)
    partitioned = partition1(ll, item)
    print(partitioned)
    assert partitioned.array() == expected


pytest.main()
