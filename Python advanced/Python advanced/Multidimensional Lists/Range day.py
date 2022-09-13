import sys


def shoot(matrix, dir):
    global shot_targets
    global left_targets
    if dir == 'up':
        for i in range(row, -1, -1):
            if matrix[i][col] == 'x':
                left_targets -= 1
                shot_targets += 1
                matrix[i][col] = '.'
                targets_positions.append([i, col])
                if left_targets == 0:
                    print(f'Training completed! All {shot_targets} targets hit.')
                    for j in targets_positions:
                        print(j)
                    sys.exit()
                else:
                    return
    elif dir == 'down':
        for i in range(row, 5):
            if matrix[i][col] == 'x':
                left_targets -= 1
                shot_targets += 1
                matrix[i][col] = '.'
                targets_positions.append([i, col])
                if left_targets == 0:
                    print(f'Training completed! All {shot_targets} targets hit.')
                    for j in targets_positions:
                        print(j)
                    sys.exit()
                else:
                    return
    elif dir == 'left':
        for i in range(col, -1, -1):
            if matrix[row][i] == 'x':
                left_targets -= 1
                shot_targets += 1
                matrix[row][i] = '.'
                targets_positions.append([row, i])
                if left_targets == 0:
                    print(f'Training completed! All {shot_targets} targets hit.')
                    for j in targets_positions:
                        print(j)
                    sys.exit()
                else:
                    return
    elif dir == 'right':
        for i in range(col, 5):
            if matrix[row][i] == 'x':
                left_targets -= 1
                shot_targets += 1
                matrix[row][i] = '.'
                targets_positions.append([row, i])
                if left_targets == 0:
                    print(f'Training completed! All {shot_targets} targets hit.')
                    for j in targets_positions:
                        print(j)
                    sys.exit()
                else:
                    return


def move(matrix, dir, steps):
    global row
    global col
    if dir == 'up':
        if row - steps < 0:
            return
        if matrix[row - steps][col] != 'x':
            row -= steps
    elif dir == 'down':
        if row + steps >= 5:
            return
        if matrix[row + steps][col] != 'x':
            row += steps
    elif dir == 'left':
        if col - steps < 0:
            return
        if matrix[row][col - steps] != 'x':
            col -= steps
    elif dir == 'right':
        if col + steps >= 5:
            return
        if matrix[row][col + steps] != 'x':
            col += steps



matrix = [[x for x in input().split(' ')] for _ in range(5)]
n = int(input())
left_targets = 0
shot_targets = 0
targets_positions = []
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'A':
            row = i
            col = j
        if matrix[i][j] == 'x':
            left_targets += 1

for _ in range(n):
    command = input().split(' ')
    if command[0] == 'move':
        move(matrix, command[1], int(command[2]))
    elif command[0] == 'shoot':
        shoot(matrix, command[1])

print(f'Training not completed! {left_targets} targets left.')
for i in targets_positions:
    print(i)
