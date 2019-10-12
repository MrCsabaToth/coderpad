class Node(object):
    next = None
    data = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        tracker = dict()
        n = self
        ret = "[{}".format(n.data)
        while n.next != None:
            if n in tracker:
                ret += "***"
                break

            tracker[n] = True
            n = n.next
            ret += ", {}".format(n.data)

        ret += "]"
        return ret

    def append(self, data):
        tracker = dict()
        end = Node(data)
        n = self
        while n.next != None:
            if n.next in tracker:
                return

            tracker[n] = True
            n = n.next

        n.next = end

    def array(self):
        tracker = dict()
        n = self
        lst = [n.data]
        while n.next != None:
            if n.next in tracker:
                break

            tracker[n] = True
            n = n.next
            lst.append(n.data)

        return lst

    def get(self, i):
        tracker = dict()
        j = 0
        ll = self
        while j < i and ll:
            if ll in tracker:
                break

            tracker[ll] = True
            ll = ll.next
            j += 1

        return ll

    def len(self):
        tracker = dict()
        i = 0
        ll = self
        while ll:
            if ll in tracker:
                return -1

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

def build_random(n):
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


def get_loop(ll):
    tracker = dict()
    while ll:
        if ll in tracker:
            return ll

        tracker[ll] = True
        ll = ll.next

    return None


def get_loop2(ll):
    fast = ll
    slow = ll
    start = True
    while slow.next:
        if fast == slow and not start:
            break

        start = False

        if not fast.next or not fast.next.next:
            return None

        slow = slow.next
        fast = fast.next.next

    slow = ll
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return slow


@pytest.mark.parametrize("i", range(5))
def test_intersect1(i):
    n = random.randint(10, 20)
    ll = build_random(n)
    make_loop = random.randint(0, 10) % 2 == 1
    expected = None
    if make_loop:
        i1 = random.randint(1, n - 1)
        i2 = random.randint(1, n - 1)
        il1 = ll.get(i1)
        il2 = ll.get(i2)
        print(i1, il1.data if il1 else None, i2, il2.data if il2 else None, ll)
        if i1 > i2:
            il1.next = il2
            expected = il2
        else:
            il2.next = il1
            expected = il1

    assert get_loop(ll) == expected
    assert get_loop2(ll) == expected


pytest.main()
