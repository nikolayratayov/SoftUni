import re


a = input()
a = a.replace(' ', '')
a = a.split(',')
demons = {}
for i in a:
    health = 0
    for j in i:
        if ord(j) < 42 or ord(j) > 57:
            health += ord(j)
    damage = re.findall(r'[-]?[0-9]+(?:\.[0-9]+)?', i)
    damage_number = 0
    for j in damage:
        damage_number += float(j)
    for j in i:
        if j == '*':
            damage_number *= 2
        elif j == '/':
            damage_number /= 2
    demons[i] = [health, damage_number]

demons_sorted = {k: v for k, v in sorted(demons.items(), key=lambda item: item[0])}
for k, v in demons_sorted.items():
    print(f'{k} - {v[0]} health, {v[1]:.2f} damage')
