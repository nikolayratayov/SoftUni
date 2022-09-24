def check_diag(row, col, matrix):
    if row <= -1 or col <= -1 or row >= 8 or col >= 8:
        return False
    elif matrix[row][col] == 'Q':
        return True
    return False


matrix = []
for i in range(8):
    matrix.append([x for x in input().split(' ')])

res = []
for i in range(8):
    for j in range(8):
        if matrix[i][j] == 'K':
            row = i
            col = j

for i in range(1, 8):
    if check_diag(row - i, col - i, matrix):
        res.append([row - i, col - i])
        break

for i in range(1, 8):
    if check_diag(row - i, col + i, matrix):
        res.append([row - i, col + i])
        break

for i in range(1, 8):
    if check_diag(row + i, col + i, matrix):
        res.append([row + i, col + i])
        break

for i in range(1, 8):
    if check_diag(row + i, col - i, matrix):
        res.append([row + i, col - i])
        break

for i in range(row, -1, -1):
    if matrix[i][col] == 'Q':
        res.append([i, col])
        break

for i in range(col, 8):
    if matrix[row][i] == 'Q':
        res.append([row, i])
        break

for i in range(row, 8):
    if matrix[i][col] == 'Q':
        res.append([i, col])
        break

for i in range(col, -1, -1):
    if matrix[row][i] == 'Q':
        res.append([row, i])
        break

if len(res) == 0:
    print('The king is safe!')
else:
    for i in res:
        print(i)
