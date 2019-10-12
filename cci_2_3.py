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


def delmid1(ll, item):
    prev = ll
    ll = ll.next
    while ll:
        if ll.data == item:
            prev.next = ll.next
            return

        prev = ll
        ll = ll.next


def delmid2(item):
    if not item.next:
        return

    item.data = item.next.data
    item.next = item.next.next


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


import copy
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


@pytest.mark.parametrize("array", [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_delmid1(array):
    n = len(array)

    for i in range(1, n - 1):
        array2 = copy.copy(array)
        item = array[i]
        print(i, item)
        ll = build(array)
        delmid1(ll, item)
        array2.remove(item)
        assert ll.array() == array2


@pytest.mark.parametrize("array", [
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_delmid2(array):
    n = len(array)

    for i in range(n - 1):
        array2 = copy.copy(array)
        ll = build(array)
        item = ll.get(i)
        item_data = item.data
        delmid2(item)
        array2.remove(item_data)
        print(i, array, ll, item_data, array2)
        assert ll.array() == array2


pytest.main()
