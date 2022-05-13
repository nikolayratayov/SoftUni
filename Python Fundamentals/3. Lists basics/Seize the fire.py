neshtosi = input()
voda = int(input())
neshtosi = list(neshtosi.split('#'))

effort = 0
total_fire = 0
print('Cells:')
for i in neshtosi:
    if 'High' in i:
        vremenno = list(i.split(' = '))
        x = int(vremenno[1])
        if 81 <= x <= 125:
            if voda < x:
                continue
            voda -= x
            effort += 0.25 * x
            total_fire += x
            print(f' - {x}')
    elif 'Medium' in i:
        vremenno = list(i.split(' = '))
        x = int(vremenno[1])
        if 51 <= x <= 80:
            if voda < x:
                continue
            voda -= x
            effort += 0.25 * x
            total_fire += x
            print(f' - {x}')
    elif 'Low' in i:
        vremenno = list(i.split(' = '))
        x = int(vremenno[1])
        if 1 <= x <= 50:
            if voda < x:
                continue
            voda -= x
            effort += 0.25 * x
            total_fire += x
            print(f' - {x}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')