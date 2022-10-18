import  sys


def move(row, col, matrix):
    global water
    global metal
    global beton
    global current_col
    global current_row
    if row == -1:
        row = 5
    if row == 6:
        row = 0
    if col == -1:
        col = 5
    if col == 6:
        col = 0
    if matrix[row][col] == 'R':
        print(f'Rover got broken at ({row}, {col})')
        print('Area not suitable to start the colony.')
        sys.exit()
    elif matrix[row][col] == 'W':
        print(f'Water deposit found at ({row}, {col})')
        water += 1
        matrix[row][col] = '-'
        current_row = row
        current_col = col
    elif matrix[row][col] == 'M':
        print(f'Metal deposit found at ({row}, {col})')
        metal += 1
        matrix[row][col] = '-'
        current_row = row
        current_col = col
    elif matrix[row][col] == 'C':
        print(f'Concrete deposit found at ({row}, {col})')
        beton += 1
        matrix[row][col] = '-'
        current_row = row
        current_col = col
    else:
        current_row = row
        current_col = col


water = 0
metal = 0
beton = 0
matrix = []
for i in range(6):
    matrix.append([x for x in input().split(' ')])

for i in range(6):
    for j in range(6):
        if matrix[i][j] == 'E':
            current_row = i
            current_col = j

commands = [x for x in input().split(', ')]

for i in commands:
    if i == 'up':
        move(current_row - 1, current_col, matrix)
    elif i == 'right':
        move(current_row, current_col + 1, matrix)
    elif i == 'down':
        move(current_row + 1, current_col, matrix)
    elif i == 'left':
        move(current_row, current_col - 1, matrix)

if water > 0 and metal > 0 and beton > 0:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
