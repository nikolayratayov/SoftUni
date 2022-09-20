def math_operations(*args, **kwargs):
    count = 0
    for i in args:
        count += 1
        if count == 5:
            count = 1
        if count == 1:
            kwargs['a'] += i
        elif count == 2:
            kwargs['s'] -= i
        elif count == 3:
            try:
                kwargs['d'] /= i
            except:
                pass
        elif count == 4:
            kwargs['m'] *= i
    mydict = {k: v for k, v in sorted(kwargs.items())}
    mydict = {k:v for k, v in sorted(mydict.items(), key=lambda x: x[1], reverse=True)}
    res = ''
    for k, v in mydict.items():
        res += '\n' + f'{k}: {v:.1f}'
    return res[1:]
