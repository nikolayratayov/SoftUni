def age_assignment(*args, **kwargs):
    mydict = {}
    for i in args:
        letter = i[0]
        for k, v in kwargs.items():
            if letter == k:
                mydict[i] = v
    mydict = {k: v for k, v in sorted(mydict.items())}
    res = ''
    for k, v in mydict.items():
        res += '\n' + f'{k} is {v} years old.'
    return res[1:]
