energy = int(input())
won_battles = 0
while True:
    dist = input()
    if dist == 'End of battle':
        print(f'Won battles: {won_battles}. Energy left: {energy}')
        break
    dist = int(dist)
    if dist > energy:
        print(f'Not enough energy! Game ends with {won_battles} won battles and {energy} energy')
        break
    else:
        energy -= dist
        won_battles += 1
    if won_battles % 3 == 0:
        energy += won_battles
