mydict = {}
while True:
    a = input()
    if a.islower():
        break
    a = a.split(':')
    mydict[a[0]] = [a[1], a[2]]
if '_' in a:
    a = a.replace('_', ' ')
list_of_keys = [key for key, list_of_values in mydict.items() if a in list_of_values]

for i in list_of_keys:
    print(f'{i} - {mydict[i][0]}')
