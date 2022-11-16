def genrange(start, end):
    i = start
    while True:
        if i > end:
            break
        yield i
        i += 1
    