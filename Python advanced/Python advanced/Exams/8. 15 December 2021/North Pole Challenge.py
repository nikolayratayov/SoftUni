def move(row, col, matrix):
    global current_col
    global current_row
    global items
    global collected
    global decorations
    global gifts
    global cookies
    if row == -1:
        current_row = rows - 1
    elif row == rows:
        current_row = 0
    elif col == -1:
        current_col = cols - 1
    elif col == cols:
        current_col = 0
    else:
        current_row = row
        current_col = col
    if matrix[current_row][current_col] == 'C' or matrix[current_row][current_col] == 'D' or matrix[current_row][current_col] == 'G':
        collected += 1
        if matrix[current_row][current_col] == 'C':
            cookies += 1
        elif matrix[current_row][current_col] == 'D':
            decorations += 1
        else:
            gifts += 1
    matrix[current_row][current_col] = 'Y'


rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    matrix.append([x for x in input().split(' ')])
items = 0
collected = 0
gifts = 0
decorations = 0
cookies = 0
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'Y':
            current_row = i
            current_col = j
        if matrix[i][j] == 'G' or matrix[i][j] == 'C' or matrix[i][j] == 'D':
            items += 1

while True:
    if collected == items:
        break
    commands = input().split('-')
    if commands[0] == 'End':
        break
    if commands[0] == 'left':
        for i in range(int(commands[1])):
            matrix[current_row][current_col] = 'x'
            move(current_row, current_col - 1, matrix)
            if collected == items:
                break
    elif commands[0] == 'up':
        for i in range(int(commands[1])):
            matrix[current_row][current_col] = 'x'
            move(current_row - 1, current_col, matrix)
            if collected == items:
                break
    elif commands[0] == 'right':
        for i in range(int(commands[1])):
            matrix[current_row][current_col] = 'x'
            move(current_row, current_col + 1, matrix)
            if collected == items:
                break
    elif commands[0] == 'down':
        for i in range(int(commands[1])):
            matrix[current_row][current_col] = 'x'
            move(current_row + 1, current_col, matrix)
            if collected == items:
                break

if items == collected:
    print(f'Merry Christmas!')
print('You\'ve collected:')
print(f'- {decorations} Christmas decorations')
print(f'- {gifts} Gifts')
print(f'- {cookies} Cookies')
for i in matrix:
    print(' '.join(i))
