class TestIterator:

    value = 0

    def next(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


if __name__ == "__main__":
    ti = TestIterator()
    print list(ti)
