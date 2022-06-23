groceries = input().split('!')
while True:
    command = input()
    if command == 'Go Shopping!':
        break
    command = command.split(' ')
    if command[0] == 'Urgent':
        if command[1] not in groceries:
            groceries.insert(0, command[1])
    elif command[0] == 'Unnecessary':
        if command[1] in groceries:
            groceries.remove(command[1])
    elif command[0] == 'Correct':
        if command[1] in groceries:
            getindex = groceries.index(command[1])
            groceries.remove(command[1])
            groceries.insert(getindex, command[2])
    elif command[0] == 'Rearrange':
        if command[1] in groceries:
            groceries.remove(command[1])
            groceries.append(command[1])
print(', '.join(groceries))
