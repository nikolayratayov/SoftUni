matrix = []

for _ in range(6):
    matrix.append([x for x in input().split(' ')])

pos = input()
pos = pos[1:len(pos) - 1]
row, col = pos.split(', ')
row = int(row)
col = int(col)

while True:
    commands = input().split(', ')
    if commands[0] == 'Stop':
        break
    if commands[0] == 'Create':
        if commands[1] == 'up':
            row = row - 1
            if matrix[row][col] == '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'right':
            col = col + 1
            if matrix[row][col] == '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'down':
            row = row + 1
            if matrix[row][col] == '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'left':
            col = col - 1
            if matrix[row][col] == '.':
                matrix[row][col] = commands[2]
    elif commands[0] == 'Update':
        if commands[1] == 'up':
            row = row - 1
            if matrix[row][col] != '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'right':
            col = col + 1
            if matrix[row][col] != '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'down':
            row = row + 1
            if matrix[row][col] != '.':
                matrix[row][col] = commands[2]
        elif commands[1] == 'left':
            col = col - 1
            if matrix[row][col] != '.':
                matrix[row][col] = commands[2]
    elif commands[0] == 'Delete':
        if commands[1] == 'up':
            row = row - 1
            matrix[row][col] = '.'
        elif commands[1] == 'right':
            col = col + 1
            matrix[row][col] = '.'
        elif commands[1] == 'down':
            row = row + 1
            matrix[row][col] = '.'
        elif commands[1] == 'left':
            col = col - 1
            matrix[row][col] = '.'
    elif commands[0] == 'Read':
        if commands[1] == 'up':
            row = row - 1
            if matrix[row][col] != '.':
                print(matrix[row][col])
        elif commands[1] == 'right':
            col = col + 1
            if matrix[row][col] != '.':
                print(matrix[row][col])
        elif commands[1] == 'down':
            row = row + 1
            if matrix[row][col] != '.':
                print(matrix[row][col])
        elif commands[1] == 'left':
            col = col - 1
            if matrix[row][col] != '.':
                print(matrix[row][col])

for i in matrix:
    print(' '.join(i))
