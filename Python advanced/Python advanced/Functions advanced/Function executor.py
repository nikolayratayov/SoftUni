def func_executor(*args):
    res = ''
    for i in args:
        res += '\n' + f'{i[0].__name__} - {i[0](*i[1])}'
    return res[1:]
