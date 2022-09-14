def concatenate(*args, **kwargs):
    res = ''
    for i in args:
        res += i
    for i in kwargs:
        if i in res:
            res = res.replace(i, kwargs[i])
    return res
