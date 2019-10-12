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


import random

def build2(n):
    head = None
    curr = None
    while n:
        node = Node(random.randint(0, 100))
        if not head:
            head = node
            curr = node
        else:
            curr.next = node
            curr = curr.next

        n -= 1

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


def has_intersection1(l1, l2):
    while l1:
        runner = l2
        while runner:
            if l1 == runner:
                return l1

            runner = runner.next

        l1 = l1.next

    return None


def length_and_last(ll):
    if not ll:
        return 0, None

    n = 1
    while ll.next:
        n += 1
        ll = ll.next

    return n, ll


def has_intersection2(l1, l2):
    n1, l1last = length_and_last(l1)
    n2, l2last = length_and_last(l2)

    if l1last != l2last:
        return None

    if n1 > n2:
        diff = n1 - n2
        while diff:
            l1 = l1.next
            diff -= 1

    if n2 > n1:
        diff = n2 - n1
        while diff:
            l2 = l2.next
            diff -= 1

    while l1 and l2:
        if l1 == l2:
            return l1

        l1 = l1.next
        l2 = l2.next

    return None


@pytest.mark.parametrize("i", range(40))
def test_intersect1(i):
    n1 = random.randint(10, 20)
    n2 = random.randint(10, 20)
    l1 = build2(n1)
    l2 = build2(n2)
    expected = None
    make_intersect = random.randint(0, 10) % 2 == 1
    print(make_intersect, n1, n2, l1, l2)
    if make_intersect:
        i1i = random.randint(1, n1 - 1)
        i1 = l1.get(i1i)
        i2i = random.randint(1, n2 - 1)
        i2 = l2.get(i2i)
        print(i1i, i1.data if i1 else None, i2i, i2.data if i2 else None, l1, l2)
        i2.next = i1
        expected = i1

    assert has_intersection1(l1, l2) == expected
    assert has_intersection2(l1, l2) == expected


pytest.main()
