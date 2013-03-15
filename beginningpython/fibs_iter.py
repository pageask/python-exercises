class FibsIter:

    def __init__(self):
        self.a = 0
        self.b = 1

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


if __name__ == "__main__":
    fibs_iter = FibsIter()
    for i in fibs_iter:
        if i > 1000:
            print i
            break

    it = iter(fibs_iter)
    print it.next()
    print it.next()
