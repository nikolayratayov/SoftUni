n = int(input())
mydict = {}
for i in range(n):
    a = input().split(' ')
    type = a[0]
    name = a[1]
    damage = a[2]
    if damage == 'null':
        damage = 45
    health = a[3]
    if health == 'null':
        health = 250
    armor = a[4]
    if armor == 'null':
        armor = 10
    if type not in mydict:
        mydict[type] = {name: [damage, health, armor]}
    elif type in mydict and name not in mydict[type]:
        mydict[type][name] = [damage, health, armor]
    elif type in mydict and name in mydict[type]:
        mydict[type][name] = [damage, health, armor]

sorted_mydict = {x: {k: v for k, v in sorted(mydict[x].items(), key=lambda item: item[0])} for x in mydict}

for k, v in sorted_mydict.items():
    sum_damage = 0
    sum_healt = 0
    sum_armor = 0
    count = 0
    for i, j in v.items():
        sum_damage += int(j[0])
        sum_healt += int(j[1])
        sum_armor += int(j[2])
        count += 1
    av_damage = sum_damage / count
    av_healt = sum_healt / count
    av_armor = sum_armor / count
    print(f'{k}::({av_damage:.2f}/{av_healt:.2f}/{av_armor:.2f})')
    for i, j in v.items():
        print(f'-{i} -> damage: {j[0]}, health: {j[1]}, armor: {j[2]}')
