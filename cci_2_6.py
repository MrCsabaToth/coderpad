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

    def len(self):
        i = 0
        ll = self
        while ll:
            i += 1
            ll = ll.next

        return i

    def revrec(self):
        node = Node(self.data)
        if not self.next:
            return node, node

        head, ret = self.next.revrec()
        ret.next = node
        return head, node

    def reverse(self):
        head, ret = self.revrec()
        return head


def ispal(ll):
    n = ll.len()
    rev = ll.reverse()
    for i in range(n // 2 + 1):
        if ll.data != rev.data:
            return False

        ll = ll.next
        rev = rev.next

    return True


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
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_len(array):
    ll = build(array)

    assert ll.len() == len(array)


@pytest.mark.parametrize("array", [
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_reverse(array):
    ll = build(array)

    assert ll.reverse().array() == array[::-1]


@pytest.mark.parametrize("array,expected", [
    ([1], True),
    ([7, 1], False),
    ([7, 7], True),
    ([7, 1, 7], True),
    ([7, 1, 1, 7], True),
    ([7, 1, 7, 6], False),
    ([7, 1, 6, 1, 7], True),
    ([7, 1, 6, 1, 1], False),
])
def test_partition(array, expected):
    ll = build(array)
    print(ll, ll.reverse())
    print(ll)
    assert ispal(ll) == expected


pytest.main()
