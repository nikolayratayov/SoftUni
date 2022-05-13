a = input()
alist = list(a.split(' '))

while True:
    kom = input()
    if kom == 'No Money':
        break

    komlist = list(kom.split(' '))

    if komlist[0] == 'OutOfStock':
        for i in alist:
            if i == komlist[1]:
                alist[alist.index(komlist[1])] = None

    if komlist[0] == 'Required':
        if 0 <= int(komlist[2]) < len(alist):
            alist[int(komlist[2])] = komlist[1]

    if komlist[0] == 'JustInCase':
        alist[len(alist) - 1] = komlist[1]

for i in alist:
    if i is None:
        continue
    if i == len(alist) - 1:
        print(i)
        break
    print(f'{i}', end=' ')
