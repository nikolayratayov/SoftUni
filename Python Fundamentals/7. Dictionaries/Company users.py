mydict = {}
while True:
    a = input()
    if a == 'End':
        break
    a = a.split(' -> ')
    if a[0] not in mydict:
        mydict[a[0]] = list()
        mydict[a[0]].append(a[1])
    else:
        if a[1] in mydict[a[0]]:
            pass
        else:
            mydict[a[0]].append(a[1])

for i in mydict:
    print(i)
    for j in mydict[i]:
        print(f'-- {j}')
