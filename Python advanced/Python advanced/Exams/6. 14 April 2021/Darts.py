import sys


def check_winner():
    if points_1 <= 0:
        print(f'{player_1} won the game with {count_1} throws!')
        sys.exit()
    elif points_2 <= 0:
        print(f'{player_2} won the game with {count_2} throws!')
        sys.exit()
    return


def decrease_points(row, col, matrix):
    global player
    global points_1
    global points_2
    global count_1
    global count_2
    if row >= 7 or col >= 7:
        return
    if matrix[row][col] == 'B':
        if player == 1:
            points_1 -= 501
            check_winner()
        else:
            points_2 -= 501
            check_winner()
    elif matrix[row][col] == 'T':
        suma = int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
        if player == 1:
            points_1 -= suma * 3
            check_winner()
        else:
            points_2 -= suma * 3
            check_winner()
    elif matrix[row][col] == 'D':
        suma = int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6])
        if player == 1:
            points_1 -= suma * 2
            check_winner()
        else:
            points_2 -= suma * 2
            check_winner()
    else:
        if player == 1:
            points_1 -= int(matrix[row][col])
            check_winner()
        else:
            points_2 -= int(matrix[row][col])
            check_winner()


player_1, player_2 = [x for x in input().split(', ')]
matrix = []
count_1 = 0
count_2 = 0
points_1 = 501
points_2 = 501
player = 1
for _ in range(7):
    matrix.append([x for x in input().split(' ')])
while True:
    row, col = [int(x) for x in input().lstrip('(').rstrip(')').split(', ')]
    if player == 1:
        count_1 += 1
    else:
        count_2 += 1
    decrease_points(row, col, matrix)
    if player == 1:
        player = 2
    else:
        player = 1
