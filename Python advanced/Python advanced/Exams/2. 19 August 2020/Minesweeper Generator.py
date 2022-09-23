def check_bomb(row, col, matrix):
    if row == -1 or row == len(matrix) or col == -1 or col == len(matrix):
        return 0
    if matrix[row][col] == '*':
        return 1
    return 0


def check_num(row, col, matrix):
    count_bombs = 0
    if matrix[row][col] == '*':
        return '*'
    count_bombs += check_bomb(row, col - 1, matrix)
    count_bombs += check_bomb(row - 1, col - 1, matrix)
    count_bombs += check_bomb(row - 1, col, matrix)
    count_bombs += check_bomb(row - 1, col + 1, matrix)
    count_bombs += check_bomb(row, col + 1, matrix)
    count_bombs += check_bomb(row + 1, col + 1, matrix)
    count_bombs += check_bomb(row + 1, col, matrix)
    count_bombs += check_bomb(row + 1, col - 1, matrix)
    return count_bombs


size = int(input())
bombs = int(input())
matrix = []
for i in range(size):
    matrix.append(['-'] * size)
for i in range(bombs):
    x, y = input().lstrip('(').rstrip(')').split(', ')
    matrix[int(x)][int(y)] = '*'
for row in range(size):
    for col in range(size):
        matrix[row][col] = check_num(row, col, matrix)
for i in matrix:
    print(' '.join(str(x) for x in i))
