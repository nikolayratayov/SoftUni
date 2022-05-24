mydict = {}
mydict['shards'] = 0
mydict['fragments'] = 0
mydict['motes'] = 0
stop = False
while True:
    if stop:
        break
    a = input().lower().split(' ')
    for i in range(0, len(a) - 1, 2):
        if a[i + 1] in mydict:
            temp = int(mydict[a[i + 1]]) + int(a[i])
            mydict[a[i + 1]] = temp
        else:
            mydict[a[i + 1]] = int(a[i])
        if 'shards' in mydict and mydict['shards'] >= 250:
            mydict['shards'] -= 250
            print(f'Shadowmourne obtained!')
            stop = True
            break
        if 'fragments' in mydict and mydict['fragments'] >= 250:
            mydict['fragments'] -= 250
            print(f'Valanyr obtained!')
            stop = True
            break
        if 'motes' in mydict and mydict['motes'] >= 250:
            mydict['motes'] -= 250
            print(f'Dragonwrath obtained!')
            stop = True
            break
print(f'shards: {mydict.get("shards")}')
print(f'fragments: {mydict.get("fragments")}')
print(f'motes: {mydict.get("motes")}')
for i in mydict:
    if i != 'shards' and i != 'fragments' and i != 'motes':
        print(f'{i}: {mydict.get(i)}')
