a = input().split(' ')
while True:
    b = input()
    if b == '3:1':
        break
    b = b.split(' ')
    if b[0] == 'merge':
        if int(b[1]) < -len(a):
            a[: int(b[2]) + 1] = [''.join(a[: int(b[2]) + 1])]
        elif int(b[1]) < 0 and 0 <= int(b[2]) < len(a):
            a[:int(b[2]) + 1] = [''.join(a[:int(b[2]) + 1])]
        else:
            a[int(b[1]): int(b[2]) + 1] = [''.join(a[int(b[1]): int(b[2]) + 1])]
    elif b[0] == 'divide':
        takestr = a[int(b[1])]
        a.pop(int(b[1]))

        portions = len(takestr) // int(b[2])
        count = 0
        take = ''
        nqkavlist = []
        dobaveni = 0
        for i in takestr:
            count += 1
            take += i
            if dobaveni == int(b[2]) - 1:
                continue
            if count == portions:
                nqkavlist.append(take)
                take = ''
                count = 0
                dobaveni += 1
        nqkavlist.append(take)
        for i in reversed(nqkavlist):
            a.insert(int(b[1]), i)

print(' '.join(a))
