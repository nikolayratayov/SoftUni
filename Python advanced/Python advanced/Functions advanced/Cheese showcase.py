def sorting_cheeses(**kwargs):
    kwargs = {k: v for k, v in sorted(kwargs.items())}
    kwargs = {k: v for k, v in sorted(kwargs.items(), key=lambda x: len(x[1]), reverse=True)}
    res = ''
    for k, v in kwargs.items():
        res += k + '\n'
        for i in sorted(v, reverse=True):
            res += str(i) + '\n'
    return res[:len(res) - 1]
