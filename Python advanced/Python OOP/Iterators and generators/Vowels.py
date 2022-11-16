class vowels:
    vowels = "AaEeIiOoUu"

    def __init__(self, word):
        self.word = word
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.word):
            raise StopIteration
        elif self.word[self.i] in vowels.vowels:
            return self.word[self.i]
        else:
            return vowels.__next__(self)
