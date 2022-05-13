import copy


def check(row, col):
    global already_checked
    # left
    if col == 0:
        pass
    else:
        if field[row][col - 1] == '.':
            a = [row, col - 1]
            if a not in already_checked:
                already_checked.append(a)
                check(row, col - 1)
    # right
    if col == (len(field[row]) - 1):
        pass
    else:
        if field[row][col + 1] == '.':
            a = [row, col + 1]
            if a not in already_checked:
                already_checked.append(a)
                check(row, col + 1)
    # up
    if row == 0:
        pass
    else:
        if field[row - 1][col] == '.':
            a = [row - 1, col]
            if a not in already_checked:
                already_checked.append(a)
                check(row - 1, col)
    # down
    if row == (len(field) - 1):
        pass
    else:
        if field[row + 1][col] == '.':
            a = [row + 1, col]
            if a not in already_checked:
                already_checked.append(a)
                check(row + 1, col)


def check_neighbour(row, col):
    global already_checked
    already_checked = []
    check(row, col)
    return already_checked



n = int(input())
field = []
for i in range(n):
    a = input().split(' ')
    field.append(a)


broi = []
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '.':
            a = check_neighbour(i, j)
            if len(a) > len(broi):
                broi = copy.copy(a)

print(len(broi))