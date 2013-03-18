from itertools import islice
from itertools import takewhile


def check_key(key):
    if not isinstance(key, (int, long)):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:

    def __init__(self, start, step):
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_key(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + self.step * key

    def __setitem__(self, key, value):
        check_key(key)
        self.changed[key] = value

    def gen(self):
        i = 0
        while True:
            yield self[i]
            i += 1


if __name__ == "__main__":
    s = ArithmeticSequence(1, 2)
    print list(islice(s.gen(), 11))
    print list(takewhile(lambda e: e < 10, s.gen()))
    print s[4]
    print s[4]
    s[4] = 2
    print s[4]
    print s[5]
