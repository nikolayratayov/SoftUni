class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.i = 0 - self.step
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.count:
            self.i += self.step
            self.counter += 1
            return self.i
        else:
            raise StopIteration
