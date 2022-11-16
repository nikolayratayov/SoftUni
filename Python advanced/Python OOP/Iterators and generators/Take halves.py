def solution():
    def integers():
        i = 0
        while True:
            i += 1
            yield i

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        lst = []
        counter = 0
        for i in seq:
            counter += 1
            if counter > n:
                break
            lst.append(i)
        return lst


    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
