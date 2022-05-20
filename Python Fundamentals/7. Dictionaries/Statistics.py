mydict = {}
while True:
    a = input()
    if a == 'statistics':
        break
    a = a.split(': ')
    if a[0] not in mydict:
        mydict[a[0]] = int(a[1])
    else:
        temp = mydict[a[0]] + int(a[1])
        mydict[a[0]] = temp
sumata = 0
print('Products in stock:')
for i in mydict:
    print(f'- {i}: {mydict[i]}')
    sumata += mydict[i]

print(f'Total Products: {len(mydict)}')
print(f'Total Quantity: {sumata}')



# myd = {'a': 1, 'b': 2}
# for i in myd:
#     print(i, myd[i])