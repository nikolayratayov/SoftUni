mydict = {}
while True:
    a = input()
    if a == 'buy':
        break
    a = a.split(' ')
    if a[0] not in mydict:
        mydict[a[0]] = [float(a[1]), int(a[2])]
    else:
        quantity = mydict[a[0]][1]
        mydict[a[0]] = [float(a[1]), quantity + int(a[2])]
for i, j in mydict.items():
    print(f'{i} -> {(j[0] * j[1]):.2f}')
