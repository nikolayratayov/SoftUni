effects = [int(x) for x in input().split(', ')]
casings = [int(x) for x in input().split(', ')]
cherry = 0
datura = 0
smoke = 0
while True:
    if len(effects) == 0 or len(casings) == 0:
        print('You don\'t have enough materials to fill the bomb pouch.')
        break
    if cherry >= 3 and datura >= 3 and smoke >= 3:
        print('Bene! You have successfully filled the bomb pouch!')
        break
    suma = effects[0] + casings[-1]
    if suma == 40:
        datura += 1
        effects.pop(0)
        casings.pop()
    elif suma == 60:
        cherry += 1
        effects.pop(0)
        casings.pop()
    elif suma == 120:
        smoke += 1
        effects.pop(0)
        casings.pop()
    else:
        casings[-1] -= 5
if len(effects) > 0:
    print(f"Bomb Effects: {', '.join(str(x) for x in effects)}")
else:
    print('Bomb Effects: empty')
if len(casings) > 0:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
else:
    print('Bomb Casings: empty')
print(f'Cherry Bombs: {cherry}')
print(f'Datura Bombs: {datura}')
print(f'Smoke Decoy Bombs: {smoke}')
