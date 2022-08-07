n = int(input())
heroes = {}
for _ in range(n):
    name, hp, mana = input().split(' ')
    heroes[name] = [int(hp), int(mana)]
while True:
    command = input().split(' - ')
    if command[0] == 'End':
        break
    elif command[0] == 'CastSpell':
        if int(command[2]) <= heroes[command[1]][1]:
            heroes[command[1]][1] -= int(command[2])
            print(f'{command[1]} has successfully cast {command[3]} and now has {heroes[command[1]][1]} MP!')
        else:
            print(f'{command[1]} does not have enough MP to cast {command[3]}!')
    elif command[0] == 'TakeDamage':
        heroes[command[1]][0] -= int(command[2])
        if heroes[command[1]][0] > 0:
            print(f'{command[1]} was hit for {command[2]} HP by {command[3]} and now has {heroes[command[1]][0]} HP left!')
        else:
            print(f'{command[1]} has been killed by {command[3]}!')
            heroes.pop(command[1])
    elif command[0] == 'Recharge':
        old_mp = heroes[command[1]][1]
        heroes[command[1]][1] += int(command[2])
        if heroes[command[1]][1] > 200:
            heroes[command[1]][1] = 200
            print(f'{command[1]} recharged for {200 - old_mp} MP!')
        else:
            print(f'{command[1]} recharged for {command[2]} MP!')
    elif command[0] == 'Heal':
        old_hp = heroes[command[1]][0]
        heroes[command[1]][0] += int(command[2])
        if heroes[command[1]][0] > 100:
            heroes[command[1]][0] = 100
            print(f'{command[1]} healed for {100 - old_hp} HP!')
        else:
            print(f'{command[1]} healed for {command[2]} HP!')
for k, v in heroes.items():
    print(k)
    print(f'  HP: {v[0]}')
    print(f'  MP: {v[1]}')
