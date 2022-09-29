def check_square(row, col):
    num = 8 - row
    if col == 0:
        letter = 'a'
    elif col == 1:
        letter = 'b'
    elif col == 2:
        letter = 'c'
    elif col == 3:
        letter = 'd'
    elif col == 4:
        letter = 'e'
    elif col == 5:
        letter = 'f'
    elif col == 6:
        letter = 'g'
    else:
        letter = 'h'
    return f'{letter}{num}'


matrix = []
for _ in range(8):
    matrix.append([x for x in input().split(' ')])

for row in range(8):
    for col in range(8):
        if matrix[row][col] == 'w':
            w_row = row
            w_col = col
        if matrix[row][col] == 'b':
            b_row = row
            b_col = col

while True:
    if w_col - 1 != -1:
        if matrix[w_row - 1][w_col - 1] == 'b':
            print(f'Game over! White win, capture on {check_square(w_row - 1, w_col - 1)}.')
            break
    if w_col + 1 != 8:
        if matrix[w_row - 1][w_col + 1] == 'b':
            print(f'Game over! White win, capture on {check_square(w_row - 1, w_col + 1)}.')
            break
    matrix[w_row][w_col] = '-'
    w_row -= 1
    matrix[w_row][w_col] = 'w'
    if w_row == 0:
        print(f'Game over! White pawn is promoted to a queen at {check_square(w_row, w_col)}.')
        break
    if b_col - 1 != -1:
        if matrix[b_row + 1][b_col - 1] == 'w':
            print(f'Game over! Black win, capture on {check_square(b_row + 1, b_col - 1)}.')
            break
    if b_col + 1 != 8:
        if matrix[b_row + 1][b_col + 1] == 'w':
            print(f'Game over! Black win, capture on {check_square(b_row + 1, b_col + 1)}.')
            break
    matrix[b_row][b_col] = '-'
    b_row += 1
    matrix[b_row][b_col] = 'b'
    if b_row == 7:
        print(f'Game over! Black pawn is promoted to a queen at {check_square(b_row, b_col)}.')
        break
