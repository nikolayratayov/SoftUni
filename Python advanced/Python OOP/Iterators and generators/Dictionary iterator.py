class dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.it = list(self.dictionary.items())
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.it):
            raise StopIteration
        else:
            return self.it[self.i]
        