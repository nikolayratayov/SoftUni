mydict = {}
while True:
    a = input()
    if a == 'end':
        break
    a = a.split(' : ')
    if a[0] in mydict:
        mydict[a[0]].append(a[1])
    else:
        mydict[a[0]] = list()
        mydict[a[0]].append(a[1])

for i, j in mydict.items():
    print(f'{i}: {len(j)}')
    for k in j:
        print(f'-- {k}')
