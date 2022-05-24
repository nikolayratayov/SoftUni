mydict = {}
while True:
    a = input().split('-')
    if len(a) == 1:
        break
    mydict[a[0]] = a[1]

for i in range(int(a[0])):
    name = input()
    if name in mydict:
        print(f'{name} -> {mydict.get(name)}')
    else:
        print(f'Contact {name} does not exist.')
