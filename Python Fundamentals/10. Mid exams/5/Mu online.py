health = 100
bitcoins = 0
rooms = input().split('|')
best_room = 0
success = True
for i in rooms:
    best_room += 1
    command = i.split(' ')
    if command[0] == 'potion':
        if health + int(command[1]) > 100:
            diff = 100 - health
            health = 100
        else:
            diff = int(command[1])
            health += diff
        print(f'You healed for {diff} hp.')
        print(f'Current health: {health} hp.')
    elif command[0] == 'chest':
        bitcoins += int(command[1])
        print(f'You found {command[1]} bitcoins.')
    else:
        health -= int(command[1])
        if health > 0:
            print(f'You slayed {command[0]}.')
        else:
            print(f'You died! Killed by {command[0]}.')
            print(f'Best room: {best_room}')
            success = False
            break
if success:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
