class Node(object):
    next = None
    data = None
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        n = self
        ret = str(n.data)
        while n.next != None:
            n = n.next
            ret += ", {}".format(n.data)

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


def remdup1(ll):
    if not ll:
        return

    indicator = dict()
    prev = None
    while ll:
        if ll.data in indicator:
            if prev:
                prev.next = ll.next
        else:
            indicator[ll.data] = True
            prev = ll

        ll = ll.next


def remdup2(ll):
    if not ll or not ll.next:
        return

    indicator = dict()
    prev = ll
    ll = ll.next
    if prev.data == ll.data:
        prev.next = ll.next

    while ll:
        if ll.data in indicator:
            prev.next = ll.next
        else:
            indicator[ll.data] = True
            prev = ll

        ll = ll.next


def remdup3(ll):
    head = ll
    prev = None
    while ll:
        firstof = None
        runner = head
        while runner:
            if runner.data == ll.data:
                firstof = runner
                break

            runner = runner.next

        if firstof != ll:
            if prev:
                prev.next = ll.next
        else:
            prev = ll

        ll = ll.next


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


@pytest.mark.parametrize("array,expected", [
    ([1], [1]),
    ([1, 2], [1, 2]),
    ([1, 1], [1]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 1, 3], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
])
def test_remdup(array, expected):
    ll = build(array)
    remdup1(ll)
    assert ll.array() == expected

    ll = build(array)
    remdup2(ll)
    assert ll.array() == expected

    ll = build(array)
    remdup3(ll)
    assert ll.array() == expected


pytest.main()
