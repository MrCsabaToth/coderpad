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


def kth1(ll, k):
    if not ll:
        return None

    i = 0
    kth = [None] * k
    while ll:
        kth[i % k] = ll.data
        i += 1
        ll = ll.next

    if i < k:
        return None

    return kth[(i - k) % k]


def kth2(ll, length, k):
    if not ll or k > length:
        return None

    i = 0
    kth = length - k
    while ll and i < kth:
        i += 1
        ll = ll.next

    return ll.data


def kth3(ll, k):
    if not ll:
        return None

    i = 0
    kth = ll
    while ll:
        if i >= k:
            kth = kth.next

        i += 1
        ll = ll.next
        print(i, ll, kth)

    return kth.data if i >= k else None


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
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6],
])
def test_remdup(array):
    n = len(array)
    ll = build(array)

    for k in range(1, n + 3):
        print(k)
        expected = array[-k] if k < n + 1 else None
        assert kth1(ll, k) == expected
        assert kth2(ll, n, k) == expected
        assert kth3(ll, k) == expected


pytest.main()
