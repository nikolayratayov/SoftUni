def even_odd_filter(**kwargs):
    mydict = {}
    for k, v in kwargs.items():
        mydict[k] = []
        for i in v:
            if k == 'even':
                if i % 2 == 0:
                    mydict[k].append(i)
            else:
                if i % 2 != 0:
                    mydict[k].append(i)
    mydict = {k: v for k, v in sorted(mydict.items(), key=lambda x: len(x[1]))}
    return mydict
