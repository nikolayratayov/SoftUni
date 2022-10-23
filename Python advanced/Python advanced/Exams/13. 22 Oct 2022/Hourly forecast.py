def forecast(*args):
    mydict = {'Sunny': [],
              'Cloudy': [],
              'Rainy': []}
    for i in args:
        mydict[i[1]].append(i[0])

    res = ''
    for k, v in mydict.items():
        for weath in sorted(v):
            res += f'{weath} - {k}\n'
    return res[0:len(res) - 1]
