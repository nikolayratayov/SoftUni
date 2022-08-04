n = int(input())
pieces = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = []
    pieces[piece].append(composer)
    pieces[piece].append(key)
while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split('|')
    if command[0] == 'Add':
        if command[1] not in pieces:
            pieces[command[1]] = []
            pieces[command[1]].append(command[2])
            pieces[command[1]].append(command[3])
            print(f'{command[1]} by {command[2]} in {command[3]} added to the collection!')
        else:
            print(f'{command[1]} is already in the collection!')
    elif command[0] == 'Remove':
        if command[1] in pieces:
            pieces.pop(command[1])
            print(f'Successfully removed {command[1]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
    elif command[0] == 'ChangeKey':
        if command[1] in pieces:
            pieces[command[1]][1] = command[2]
            print(f'Changed the key of {command[1]} to {command[2]}!')
        else:
            print(f'Invalid operation! {command[1]} does not exist in the collection.')
for k, v in pieces.items():
    print(f'{k} -> Composer: {v[0]}, Key: {v[1]}')
