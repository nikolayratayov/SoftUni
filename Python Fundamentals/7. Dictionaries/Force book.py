mydict = {}
while True:
    vhod = input()
    if vhod == 'Lumpawaroo':
        break
    a = vhod.split(' | ')
    if len(a) > 1:
        if a[0] in mydict and a[1] in mydict[a[0]]:
            continue
        ima = False
        for i, j in mydict.items():
            if a[1] in j:
                ima = True
        if a[0] not in mydict and not ima:
            mydict[a[0]] = list()
            mydict[a[0]].append(a[1])
        elif a[0] in mydict and not ima:
            mydict[a[0]].append(a[1])
    else:
        a = vhod.split(' -> ')
        ima = False
        for i, j in mydict.items():
            if a[0] in j:
                ima = True
        if a[1] not in mydict and not ima:
            mydict[a[1]] = list()
            mydict[a[1]].append(a[0])
        elif a[1] in mydict and not ima:
            mydict[a[1]].append(a[0])
        elif ima:
            stop = False
            for i, j in mydict.items():
                for k in j:
                    if k == a[0]:
                        mydict[i].remove(k)
                        if a[1] in mydict:
                            mydict[a[1]].append(a[0])
                        else:
                            mydict[a[1]] = list()
                            mydict[a[1]].append(a[0])
                        stop = True
                        break
                if stop:
                    break

        print(f'{a[0]} joins the {a[1]} side!')

for i, j in mydict.items():
    if len(j) < 1:
        continue
    print(f'Side: {i}, Members: {len(j)}')
    for k in j:
        print(f'! {k}')
