n = int(input())
mydict = {}
for i in range(n):
    a = input().split(' ')
    if a[0] == 'register':
        if a[1] in mydict:
            print(f'ERROR: already registered with plate number {mydict[a[1]]}')
        else:
            mydict[a[1]] = a[2]
            print(f'{a[1]} registered {a[2]} successfully')
    elif a[0] == 'unregister':
        if a[1] not in mydict:
            print(f'ERROR: user {a[1]} not found')
        else:
            del mydict[a[1]]
            print(f'{a[1]} unregistered successfully')
for i, j in mydict.items():
    print(f'{i} => {j}')
    