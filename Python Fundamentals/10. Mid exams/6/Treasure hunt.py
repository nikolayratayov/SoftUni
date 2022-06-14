loots = input().split('|')
while True:
    command = input()
    if command == 'Yohoho!':
        break
    command = command.split(' ')
    if command[0] == 'Loot':
        end = len(command) - 1
        for i in range(1, end + 1):
            if command[i] not in loots:
                loots.insert(0, command[i])
    elif command[0] == 'Drop':
        if int(command[1]) in range(-len(loots), len(loots)):
            temp = loots.pop(int(command[1]))
            loots.append(temp)
    elif command[0] == 'Steal':
        stolen = []
        if int(command[1]) >= len(loots):
            print(', '.join(loots))
            loots = []
        else:
            end = -int(command[1]) - 1
            for i in range(-1, end, -1):
                stolen.append(loots.pop())
            stolen_rev = list(stolen[::-1])
            print(', '.join(stolen_rev))
if len(loots) == 0:
    print('Failed treasure hunt.')
else:
    suma = 0
    for i in loots:
        suma += len(i)
    average = suma / len(loots)
    print(f'Average treasure gain: {average:.2f} pirate credits.')
