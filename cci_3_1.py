class StackN(list):
    _parts = []
    
    def __init__(self, nparts):
        super().__init__()
        self._parts = range(1, nparts + 1)

    def pushn(self, part, item):
        if part not in self._parts:
            return None
    
        self.append((part, item))

    def is_empty(self, part):
        return not any(item[0] == part for item in self)

    def len(self, part):
        return len(item[0] == part for item in self)

    def popn(self, part):
        if part not in self._parts:
            return None

        item = None
        popped = list()
        while not item and len(self):
            top = self.pop()
            if top[0] == part:
                item = top[1]
            else:
                popped.append(top)

        if popped:
            popped.reverse()
            self.extend(popped)
        
        return item

    def peekn(self, part):
        for x in reversed(self):
            if x[0] == part:
                return x[1]

        return None


import pytest
import random

def test_nsteack():
    stacks = [list(), list(), list()]
    stackn = StackN(3)
    for x in range(1000):
        n = random.randint(1, 3)
        print("n = {}".format(n))
        dir = random.randint(0, 2)
        push = (dir >= 1 and x < 500 or dir >= 2)
        if push:
            i = random.randint(0, 200)
            print("i = {}".format(i))
            stackn.pushn(n, i)
            stacks[n - 1].append(i)
            popped = stackn.peekn(n)
            assert popped == stacks[n - 1][-1]
            assert popped == i
        else:
            print("pop")
            peeked = stackn.peekn(n)
            if peeked is not None and stacks[n - 1][-1] != peeked:
                for i, stack in enumerate(stacks):
                    print("{} {}".format(i, stack))
                print(stackn)
                print("\n")

            popped = stackn.popn(n)
            if popped is not None:
                p2 = stacks[n - 1].pop()
                if popped != p2:
                    for i, stack in enumerate(stacks):
                        print("{} {}".format(i, stack))
                    print(stackn)
                assert popped == p2
            else:
                assert len(stacks[n - 1]) == 0

pytest.main()

