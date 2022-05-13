neshtosi = input()
budjet = float(input())
neshtosi = list(neshtosi.split('|'))
prodadeni = []
profit = 0
for i in neshtosi:
    if 'Clothes' in i:
        vremenno = list(i.split('->'))
        vremenno = float(vremenno[1])
        if vremenno == 0:
            continue
        if vremenno > 50:
            continue
        if budjet < vremenno:
            continue
        budjet -= vremenno
        profit += vremenno * 0.4
        vremenno += vremenno * 0.4
        prodadeni.append(vremenno)
    elif 'Shoes' in i:
        vremenno = list(i.split('->'))
        vremenno = float(vremenno[1])
        if vremenno == 0:
            continue
        if vremenno > 35:
            continue
        if budjet < vremenno:
            continue
        budjet -= vremenno
        profit += vremenno * 0.4
        vremenno += vremenno * 0.4
        prodadeni.append(vremenno)
    elif 'Accessories' in i:
        vremenno = list(i.split('->'))
        vremenno = float(vremenno[1])
        if vremenno == 0:
            continue
        if vremenno > 20.5:
            continue
        if budjet < vremenno:
            continue
        budjet -= vremenno
        profit += vremenno * 0.4
        vremenno += vremenno * 0.4
        prodadeni.append(vremenno)

for i in prodadeni:
    print(f'{i:.2f}', end=' ')
print()
print(f'Profit: {profit:.2f}')
suma = budjet + sum(prodadeni)
if suma >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
