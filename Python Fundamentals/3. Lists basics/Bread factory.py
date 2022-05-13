import sys

energy = 100
coins = 100
events = input().split('|')

for i in events:
    if 'rest' in i:
        temp = list(i.split('-'))
        temp = int(temp[1])
        if temp + energy > 100:
            gained = 100 - energy
            energy = 100
        else:
            gained = temp
            energy += gained
        print(f'You gained {gained} energy.')
        print(f'Current energy: {energy}.')
    elif 'order' in i:
        temp = list(i.split('-'))
        temp = int(temp[1])
        if energy - 30 < 0:
            if energy + 50 > 100:
                energy = 100
            else:
                energy += 50
            print('You had to rest!')
            continue
        coins += temp
        energy -= 30
        print(f'You earned {temp} coins.')
    else:
        temp = list(i.split('-'))
        cena = int(temp[1])
        ingr = temp[0]
        if cena > coins:
            print(f'Closed! Cannot afford {ingr}.')
            sys.exit()

        coins -= cena
        print(f'You bought {ingr}.')

print('Day completed!')
print(f'Coins: {coins}')
print(f'Energy: {energy}')



