def grocery_store(**kwargs):
    mydict = {k: v for k, v in sorted(kwargs.items())}
    mydict = {k: v for k, v in sorted(mydict.items(), key=lambda x: len(x[0]), reverse=True)}
    mydict = {k: v for k, v in sorted(mydict.items(), key=lambda x: x[1], reverse=True)}
    res = ''
    for k, v in mydict.items():
        res += '\n' + f'{k}: {v}'
    return res[1:]
