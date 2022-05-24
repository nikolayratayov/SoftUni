a = input()
mydict = {}
for i in a:
    if i == ' ':
        continue
    if i in mydict:
        temp = int(mydict.get(i)) + 1
        mydict[i] = temp
    else:
        mydict[i] = 1
for i in mydict:
    print(f'{i} -> {mydict.get(i)}')
