import sys


def move(r, c, matrix):
    global food
    global row
    global col
    matrix[row][col] = '.'
    row = r
    col = c
    if row == -1 or row == n or col == -1 or col == n:
        print('Game over!')
        print(f'Food eaten: {food}')
        for i in matrix:
            print(''.join(i))
        sys.exit()
    if matrix[row][col] == '*':
        food += 1
        if food == 10:
            matrix[row][col] = 'S'
            print('You won! You fed the snake.')
            print(f'Food eaten: {food}')
            for i in matrix:
                print(''.join(i))
            sys.exit()
        matrix[row][col] = '.'
    elif matrix[row][col] == 'B':
        matrix[row][col] = '.'
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 'B':
                    row = i
                    col = j
        matrix[row][col] = '.'


n = int(input())
matrix = []
food = 0
for i in range(n):
    matrix.append([x for x in list(input())])
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            row = i
            col = j

while True:
    command = input()
    if command == 'left':
        move(row, col - 1, matrix)
    elif command == 'up':
        move(row - 1, col, matrix)
    elif command == 'right':
        move(row, col + 1, matrix)
    elif command == 'down':
        move(row + 1, col, matrix)
