n = int(input())
wagons = [0 for i in range(n)]
while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' ')
    if command[0] == 'add':
        posl = wagons.pop(n - 1)
        add = posl + int(command[1])
        wagons.append(add)
    elif command[0] == 'insert':
        kade = wagons.pop(int(command[1]))
        insert = kade + int(command[2])
        wagons.insert(int(command[1]), insert)
    elif command[0] == 'leave':
        kade = wagons.pop(int(command[1]))
        ost = kade - int(command[2])
        wagons.insert(int(command[1]), ost)

print(wagons)
