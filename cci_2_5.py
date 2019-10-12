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


def add1(l1, l2):
    head = None
    sum = None
    carry = 0
    while l1 or l2:
        sumt = l1.data if l1 else 0
        sumt += l2.data if l2 else 0
        sumt += carry
        carry = 0
        if sumt > 9:
            carry = sumt // 10
            sumt -= 10

        digit = Node(sumt)
        if not sum:
            sum = digit
            head = sum
        else:
            sum.next = digit
            sum = sum.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    if carry:
        sum.next = Node(carry)

    return head


def recadd(head, ret, l1, l2, carry):
    sum = l1.data if l1 else 0
    sum += l2.data if l2 else 0
    sum += carry
    if not sum:
        return head
    
    if sum > 9:
        carry = sum // 10
        sum -= carry * 10
    else:
        carry = 0

    digit = Node(sum)
    if not head:
        head = digit
        ret = digit
    else:
        ret.next = digit
        ret = ret.next

    if l1:
        l1 = l1.next
    if l2:
        l2 = l2.next

    return recadd(head, ret, l1, l2, carry)


def add2(l1, l2):
    return recadd(None, None, l1, l2, 0)


def recadd2(l1, l2):
    l1next = l1.next if l1 else None
    l2next = l2.next if l2 else None
    sum = l1.data if l1 else 0
    sum += l2.data if l2 else 0
    ret = None
    if l1next or l2next:
        ret, carry = recadd2(l1next, l2next)
        sum += carry

    carry = 0
    if sum > 9:
        carry = sum // 10
        sum -= carry * 10

    digit = Node(sum)
    digit.next = ret

    return digit, carry


def add3(l1, l2):
    ret, carry = recadd2(l1, l2)
    if carry:
        digit = Node(carry)
        digit.next = ret
        ret = digit

    return ret


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


@pytest.mark.parametrize("l1,l2,sum", [
    ([1, 1, 1], [2, 2, 2], [3, 3, 3]),
    ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
    ([9, 7, 8], [6, 8, 5], [5, 6, 4, 1]),
    ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
    ([9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 1]),
    ([4, 5, 6], [4, 5, 6], [8, 0, 3, 1]),
    ([1, 1, 1, 0, 0], [2, 2, 2, 2, 2], [3, 3, 3, 2, 2]),
])
def test_partition(l1, l2, sum):
    added = add1(build(l1), build(l2))
    assert added.array() == sum
    added2 = add2(build(l1), build(l2))
    assert added2.array() == sum
    added3 = add3(build(l1[::-1]), build(l2[::-1]))
    assert added3.array() == sum[::-1]


pytest.main()
