items = input().split(', ')
while True:
    command = input()
    if command == 'Craft!':
        break
    command = command.split(' - ')
    if command[0] == 'Collect':
        if command[1] not in items:
            items.append(command[1])
    elif command[0] == 'Drop':
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == 'Combine Items':
        items_to_combine = command[1].split(':')
        if items_to_combine[0] in items:
            get_index = items.index(items_to_combine[0])
            items.insert(get_index + 1, items_to_combine[1])
    elif command[0] == 'Renew':
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])
print(', '.join(items))
