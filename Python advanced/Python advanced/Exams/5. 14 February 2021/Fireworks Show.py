effects = [int(x) for x in input().split(', ')]
power = [int(x) for x in input().split(', ')]
palm = 0
willow = 0
crossette = 0
while True:
    if palm >= 3 and willow >= 3 and crossette >= 3:
        print('Congrats! You made the perfect firework show!')
        break
    if len(effects) == 0 or len(power) == 0:
        print('Sorry. You can\'t make the perfect firework show.')
        break
    if effects[0] <= 0:
        effects.pop(0)
        continue
    if power[-1] <= 0:
        power.pop()
        continue
    suma = effects[0] + power[-1]
    if suma % 3 == 0 and suma % 5 != 0:
        palm += 1
        effects.pop(0)
        power.pop()
    elif suma % 5 == 0 and suma % 3 != 0:
        willow += 1
        effects.pop(0)
        power.pop()
    elif suma % 3 == 0 and suma % 5 == 0:
        crossette += 1
        effects.pop(0)
        power.pop()
    else:
        effects[0] -= 1
        effects.append(effects.pop(0))

if len(effects) > 0:
    print(f"Firework Effects left: {', '.join(str(x) for x in effects)}")
if len(power) > 0:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")
print(f'Palm Fireworks: {palm}')
print(f'Willow Fireworks: {willow}')
print(f'Crossette Fireworks: {crossette}')