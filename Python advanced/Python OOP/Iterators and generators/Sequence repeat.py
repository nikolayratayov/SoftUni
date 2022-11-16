class sequence_repeat:
    def __init__(self, word, num):
        self.num = num
        self.word = word
        self.i = -1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i == len(self.word):
            self.i = 0
        self.counter += 1
        if self.counter > self.num:
            raise StopIteration
        else:
            return self.word[self.i]
