mydict = {}
count = 0
while True:
    count += 1
    a = input()
    if a == 'stop':
        break
    if count % 2 != 0:
        rem = a
        if a not in mydict:
            mydict[a] = 0
    if count % 2 == 0:
        temp = int(mydict.get(rem)) + int(a)
        mydict[rem] = temp

for i in mydict:
    print(f'{i} -> {mydict.get(i)}')
