class StackN(list):
    _parts = []
    
    def __init__(self, nparts):
        super().__init__()
        self._parts = range(1, nparts + 1)

    def pushn(self, part, item):
        if part not in self._parts:
            return
    
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
        while item is None and len(self):
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


class StackN2(list):
    _pointers = []
    
    def __init__(self, nparts):
        super().__init__()
        self._pointers = [0] * (nparts - 1)

    def pushn(self, part, item):
        if part > len(self._pointers) or part < 1:
            return

        if part == len(self._pointers) - 1:
            self.append(item)
        else:
            self.insert(item)
            part_index = part - 1
            for i in range(part_index, len(self._pointers)):
                self._pointers[i] += 1

    def is_empty(self, part):
        if part > len(self._pointers) or part < 1:
            return False

        return (part == 1 and self._pointers[0] == 0 or
            1 < part < len(self._pointers) - 1 and self._pointers[part - 1] == self._pointers[part] or
            part == len(self._pointers) - 1 and self._pointers[part - 1] == len(self) - 1)

    def len(self, part):
        if part > len(self._pointers) or part < 1:
            return -1

        if part == 1:
            return self._pointers[0]
        elif 1 < part < len(self._pointers) - 1:
            return self._pointers[part] - self._pointers[part - 1]
        elif part == len(self._pointers) - 1:
            return len(self) - self._pointers[part - 1]

    def pointer(self, part):
        if part > len(self._pointers) or part < 1:
            return -1

        if part <= len(self._pointers):
            return self._pointers[part - 1]

        return len(self) - 1

    def popn(self, part):
        if part > len(self._pointers) or part < 1:
            return None

        if self.len(part) <= 0:
            return None

        index = self.pointer(part)
        item = self[index]
        del self[index]
        for i in range(part - 1, len(self._pointers)):
            self._pointers[i] -= 1
        
        return item

    def peekn(self, part):
        if part > len(self._pointers) or part < 1:
            return None

        if self.len(part) <= 0:
            return None

        index = self.pointer(part)
        return self[index]


import pytest
import random

def test_nsteack():
    stacks = [list(), list(), list()]
    stackn = StackN2(3)
    for x in range(1000):
        n = random.randint(1, 3)
        print("n = {}, {}".format(n, x))
        dir = random.randint(0, 2)
        push = (dir >= 1 and x < 500 or dir >= 2)
        if push:
            i = random.randint(0, 100)
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
