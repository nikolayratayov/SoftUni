import sys


def move(matrix, row, col):
    global coals
    global gained_coals
    global current_row
    global current_col
    if row < 0 or row == len(matrix) or col < 0 or col == len(matrix[0]):
        return
    if matrix[row][col] == 'e':
        print(f'Game over! ({row}, {col})')
        sys.exit()
    if matrix[row][col] == 'c':
        gained_coals += 1
        coals -= 1
        matrix[row][col] = '*'
        current_row = row
        current_col = col
        if coals == 0:
            print(f'You collected all coal! ({current_row}, {current_col})')
            sys.exit()
    current_row = row
    current_col = col


n = int(input())
moves = input().split(' ')
matrix = [[x for x in input().split(' ')] for _ in range(n)]
coals = 0
gained_coals = 0
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 's':
            current_row = row
            current_col = col
        if matrix[row][col] == 'c':
            coals += 1

for i in moves:
    if i == 'up':
        move(matrix, current_row - 1, current_col)
    elif i == 'down':
        move(matrix, current_row + 1, current_col)
    elif i == 'left':
        move(matrix, current_row, current_col - 1)
    elif i == 'right':
        move(matrix, current_row, current_col + 1)

print(f'{coals} pieces of coal left. ({current_row}, {current_col})')
