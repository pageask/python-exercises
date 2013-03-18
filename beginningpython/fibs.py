from itertools import islice
from itertools import takewhile


class Fibs:

    def gen(self):
        a, b = 1, 1
        while True:
            yield a
            a, b = b, a + b


if __name__ == "__main__":
    fibs = Fibs()
    print list(islice(fibs.gen(), 10))
    print list(takewhile(lambda f: f <= 1000, fibs.gen()))
