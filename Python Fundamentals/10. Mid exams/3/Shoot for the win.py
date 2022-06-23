targets_str = input().split(' ')
targets = [int(x) for x in targets_str]
shots = 0
while True:
    command = input()
    if command == 'End':
        break
    command = int(command)
    if command not in range(0, len(targets)):
        continue
    current_target = targets[command]
    if current_target == -1:
        continue
    targets.pop(command)
    targets.insert(command, -1)
    shots += 1
    for i in range(0, len(targets)):
        if targets[i] != -1:
            if targets[i] > current_target:
                targets[i] -= current_target
            else:
                targets[i] += current_target
print(f'Shot targets: {shots} -> ', end='')
targets_print = [str(x) for x in targets]
print(' '.join(targets_print))
