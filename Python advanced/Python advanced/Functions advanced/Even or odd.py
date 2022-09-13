def even_odd(*args):
    lst = []
    if args[-1] == 'even':
        for i in range(0, len(args) - 1):
            if args[i] % 2 == 0:
                lst.append(args[i])
    else:
        for i in range(0, len(args) - 1):
            if args[i] % 2 != 0:
                lst.append(args[i])
    return lst
