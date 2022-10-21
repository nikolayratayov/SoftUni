names = [x for x in input().split(', ')]
first = names[0]
second = names[1]

matrix = []
for _ in range(6):
    matrix.append([x for x in input().split(' ')])

turn = 1
first_break = False
second_break = False
while True:
    row, col = input().split(', ')
    row = int(row[1:])
    col = int(col[:len(col) - 1])
    if turn == 1 and first_break:
        turn = 2
        first_break = False
        continue
    if turn == 2 and second_break:
        turn = 1
        second_break = False
        continue
    if matrix[row][col] == 'E':
        if turn == 1:
            print(f'{first} found the Exit and wins the game!')
        else:
            print(f'{second} found the Exit and wins the game!')
        break
    elif matrix[row][col] == 'T':
        if turn == 1:
            print(f'{first} is out of the game! The winner is {second}.')
        else:
            print(f'{second} is out of the game! The winner is {first}.')
        break
    elif matrix[row][col] == 'W':
        if turn == 1:
            print(f'{first} hits a wall and needs to rest.')
            first_break = True
        else:
            print(f'{second} hits a wall and needs to rest.')
            second_break = True
    if turn == 1:
        turn = 2
    else:
        turn = 1
