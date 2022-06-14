import sys


pirateshipstr = input().split('>')
pirateship = [int(i) for i in pirateshipstr]
warshipstr = input().split('>')
warship = [int(i) for i in warshipstr]
maxhealth = int(input())
while True:
    command = input()
    if command == 'Retire':
        break
    command = command.split(' ')
    if command[0] == 'Fire':
        index = int(command[1])
        damage = int(command[2])
        if index in range(0, len(warship)):
            temp = warship[index] - damage
            if temp <= 0:
                print('You won! The enemy ship has sunken.')
                sys.exit()
            else:
                warship.pop(index)
                warship.insert(index, temp)
    elif command[0] == 'Defend':
        startindex = int(command[1])
        endindex = int(command[2])
        damage = int(command[3])
        if startindex in range(0, len(pirateship)) and endindex in range(0, len(pirateship)):
            for i in range(startindex, endindex + 1):
                temp = pirateship[i] - damage
                if temp <= 0:
                    print('You lost! The pirate ship has sunken.')
                    sys.exit()
                else:
                    pirateship.pop(i)
                    pirateship.insert(i, temp)
    elif command[0] == 'Repair':
        index = int(command[1])
        health = int(command[2])
        if index in range(0, len(pirateship)):
            temp = pirateship[index] + health
            if temp >= maxhealth:
                pirateship.pop(index)
                pirateship.insert(index, maxhealth)
            else:
                pirateship.pop(index)
                pirateship.insert(index, temp)
    elif command[0] == 'Status':
        count = 0
        for i in pirateship:
            if i < (0.2 * maxhealth):
                count += 1
        print(f'{count} sections need repair.')
print(f'Pirate ship status: {sum(pirateship)}')
print(f'Warship status: {sum(warship)}')
