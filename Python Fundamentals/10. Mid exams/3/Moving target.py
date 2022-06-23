targets_str = input().split(' ')
targets = [int(x) for x in targets_str]
while True:
    command = input()
    if command == 'End':
        break
    command = command.split(' ')
    if command[0] == 'Shoot':
        if int(command[1]) in range(0, len(targets)):
            targets[int(command[1])] -= int(command[2])
            if targets[int(command[1])] <= 0:
                targets.pop(int(command[1]))
    elif command[0] == 'Add':
        if int(command[1]) in range(0, len(targets)):
            targets.insert(int(command[1]), int(command[2]))
        else:
            print('Invalid placement!')
    elif command[0] == 'Strike':
        index = int(command[1])
        radius = int(command[2])
        if index - radius < 0 or index + radius >= len(targets):
            print('Strike missed!')
        else:
            for i in range((index - radius), (index + radius + 1)):
                targets.pop(index - radius)
targets_print = [str(x) for x in targets]
print('|'.join(targets_print))
