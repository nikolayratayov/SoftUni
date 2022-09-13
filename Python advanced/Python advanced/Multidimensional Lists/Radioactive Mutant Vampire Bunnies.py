import sys
import copy


def expand_with_check(matrix, row, col):
    global dead
    if row < 0 or col < 0 or row == rows or col == cols:
        return
    if matrix[row][col] == 'P':
        dead = True
    matrix[row][col] = 'B'


def expand(matrix, row, col):
    if row < 0 or col < 0 or row == rows or col == cols:
        return
    matrix[row][col] = 'B'


def move(matrix, row, col):
    global current_row
    global current_col
    if row < 0 or col < 0 or row == rows or col == cols:
        matrix[current_row][current_col] = '.'
        copy_for_loop = copy.deepcopy(matrix)
        for row_b in range(rows):
            for col_b in range(cols):
                if copy_for_loop[row_b][col_b] == 'B':
                    expand(matrix, row_b + 1, col_b)
                    expand(matrix, row_b, col_b + 1)
                    expand(matrix, row_b - 1, col_b)
                    expand(matrix, row_b, col_b - 1)
        for i in matrix:
            print(''.join(i))
        print(f'won: {current_row} {current_col}')
        sys.exit()
    matrix[current_row][current_col] = '.'
    if matrix[row][col] == 'B':
        copy_for_loop = copy.deepcopy(matrix)
        for row_b in range(rows):
            for col_b in range(cols):
                if copy_for_loop[row_b][col_b] == 'B':
                    expand(matrix, row_b + 1, col_b)
                    expand(matrix, row_b, col_b + 1)
                    expand(matrix, row_b - 1, col_b)
                    expand(matrix, row_b, col_b - 1)
        for i in matrix:
            print(''.join(i))
        print(f'dead: {row} {col}')
        sys.exit()

    current_row = row
    current_col = col
    matrix[current_row][current_col] = 'P'
    copy_for_loop = copy.deepcopy(matrix)
    for row_b in range(rows):
        for col_b in range(cols):
            if copy_for_loop[row_b][col_b] == 'B':
                expand_with_check(matrix, row_b + 1, col_b)
                expand_with_check(matrix, row_b, col_b + 1)
                expand_with_check(matrix, row_b - 1, col_b)
                expand_with_check(matrix, row_b, col_b - 1)
    if dead:
        for i in matrix:
            print(''.join(i))
        print(f'dead: {current_row} {current_col}')
        sys.exit()


dead = False
rows, cols = [int(x) for x in input().split(' ')]
matrix = [[x for x in list(input())] for _ in range(rows)]
moves = list(input())
for row in range(rows):
    for col in range(cols):
        if matrix[row][col] == 'P':
            current_row = row
            current_col = col

for i in moves:
    if i == 'U':
        move(matrix, current_row - 1, current_col)
    elif i == 'D':
        move(matrix, current_row + 1, current_col)
    elif i == 'L':
        move(matrix, current_row, current_col - 1)
    elif i == 'R':
        move(matrix, current_row, current_col + 1)
