import sys


def move(row, col, matrix, path):
    global coins
    global current_row
    global current_col
    if col == -1:
        current_col = n - 1
    elif col == n:
        current_col = 0
    elif row == -1:
        current_row = n - 1
    elif row == n:
        current_row = 0
    else:
        current_row = row
        current_col = col
    path.append([current_row, current_col])
    if matrix[current_row][current_col].isdigit():
        coins += int(matrix[current_row][current_col])
        matrix[current_row][current_col] = '-'
        if coins >= 100:
            print(f'You won! You\'ve collected {coins} coins.')
            print('Your path:')
            for i in path:
                print(i)
            sys.exit()
    elif matrix[current_row][current_col] == 'X':
        coins //= 2
        print(f'Game over! You\'ve collected {coins} coins.')
        print('Your path:')
        for i in path:
            print(i)
        sys.exit()


n = int(input())
matrix = []
coins = 0
path = []
for _ in range(n):
    matrix.append([x for x in input().split(' ')])

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'P':
            current_row = i
            current_col = j
path.append([current_row, current_col])
while True:
    command = input()
    if command == 'left':
        move(current_row, current_col - 1, matrix, path)
    elif command == 'right':
        move(current_row, current_col + 1, matrix, path)
    elif command == 'up':
        move(current_row - 1, current_col, matrix, path)
    elif command == 'down':
        move(current_row + 1, current_col, matrix, path)
