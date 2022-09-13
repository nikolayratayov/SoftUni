import sys


def check_end(presents, gived_presents, nice_kids):
    global row
    global col
    if presents == 0:
        matrix[row][col] = 'S'
        if nice_kids > 0:
            print('Santa ran out of presents!')
        for i in matrix:
            print(' '.join(i))
        if nice_kids == 0:
            print(f'Good job, Santa! {gived_presents} happy nice kid/s.')
        else:
            print(f'No presents for {nice_kids} nice kid/s.')
        sys.exit()


def cookie(matrix, row, col):
    global gived_presents
    global nice_kids
    global presents
    if matrix[row + 1][col] == 'V':
        gived_presents += 1
        nice_kids -= 1
        presents -= 1
        matrix[row + 1][col] = '-'
        check_end(presents, gived_presents, nice_kids)
    elif matrix[row + 1][col] == 'X':
        presents -= 1
        matrix[row + 1][col] = '-'
        check_end(presents, gived_presents, nice_kids)

    if matrix[row - 1][col] == 'V':
        gived_presents += 1
        nice_kids -= 1
        presents -= 1
        matrix[row - 1][col] = '-'
        check_end(presents, gived_presents, nice_kids)
    elif matrix[row - 1][col] == 'X':
        presents -= 1
        matrix[row - 1][col] = '-'
        check_end(presents, gived_presents, nice_kids)

    if matrix[row][col + 1] == 'V':
        gived_presents += 1
        nice_kids -= 1
        presents -= 1
        matrix[row][col + 1] = '-'
        check_end(presents, gived_presents, nice_kids)
    elif matrix[row][col + 1] == 'X':
        presents -= 1
        matrix[row][col + 1] = '-'
        check_end(presents, gived_presents, nice_kids)

    if matrix[row][col - 1] == 'V':
        gived_presents += 1
        nice_kids -= 1
        presents -= 1
        matrix[row][col - 1] = '-'
        check_end(presents, gived_presents, nice_kids)
    elif matrix[row][col - 1] == 'X':
        presents -= 1
        matrix[row][col - 1] = '-'
        check_end(presents, gived_presents, nice_kids)


def move(matrix, dir):
    global row
    global col
    global presents
    global nice_kids
    global gived_presents
    if dir == 'up':
        if row - 1 == -1:
            return
        matrix[row][col] = '-'
        row -= 1
        if matrix[row][col] == 'C':
            matrix[row][col] = 'S'
            cookie(matrix, row, col)
        elif matrix[row][col] == 'V':
            gived_presents += 1
            nice_kids -= 1
            presents -= 1
            check_end(presents, gived_presents, nice_kids)
        matrix[row][col] = 'S'

    elif dir == 'down':
        if row + 1 == n:
            return
        matrix[row][col] = '-'
        row += 1
        if matrix[row][col] == 'C':
            matrix[row][col] = 'S'
            cookie(matrix, row, col)
        elif matrix[row][col] == 'V':
            gived_presents += 1
            nice_kids -= 1
            presents -= 1
            check_end(presents, gived_presents, nice_kids)
        matrix[row][col] = 'S'

    elif dir == 'right':
        if col + 1 == n:
            return
        matrix[row][col] = '-'
        col += 1
        if matrix[row][col] == 'C':
            matrix[row][col] = 'S'
            cookie(matrix, row, col)
        elif matrix[row][col] == 'V':
            gived_presents += 1
            nice_kids -= 1
            presents -= 1
            check_end(presents, gived_presents, nice_kids)
        matrix[row][col] = 'S'

    elif dir == 'left':
        if col - 1 == -1:
            return
        matrix[row][col] = '-'
        col -= 1
        if matrix[row][col] == 'C':
            matrix[row][col] = 'S'
            cookie(matrix, row, col)
        elif matrix[row][col] == 'V':
            gived_presents += 1
            nice_kids -= 1
            presents -= 1
            check_end(presents, gived_presents, nice_kids)
        matrix[row][col] = 'S'


presents = int(input())
n = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(n)]
nice_kids = 0
gived_presents = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'S':
            row = i
            col = j
        if matrix[i][j] == 'V':
            nice_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break
    move(matrix, command)

for i in matrix:
    print(' '.join(i))
if nice_kids == 0:
    print(f'Good job, Santa! {gived_presents} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids} nice kid/s.')
