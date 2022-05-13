kolichestvo = int(input())
dni = int(input())

koleden_duh = 0
budjet = 0

for i in range(1, dni + 1):
    if i % 11 == 0:
        kolichestvo += 2
    if i % 2 == 0:
        budjet += kolichestvo * 2
        koleden_duh += 5
    if i % 3 == 0:
        budjet += kolichestvo * 8
        koleden_duh += 13
    if i % 5 == 0:
        budjet += 15 * kolichestvo
        koleden_duh += 17
        if i % 3 == 0:
            koleden_duh += 30
    if i % 10 == 0:
        koleden_duh -= 20
        budjet += 23

if dni % 10 == 0:
    koleden_duh -= 30

print(f'Total cost: {budjet}')
print(f'Total spirit: {koleden_duh}')
