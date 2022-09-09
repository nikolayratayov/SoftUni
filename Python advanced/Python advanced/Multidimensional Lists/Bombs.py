def decrease(matrix, damage, row, col):
    if row < 0 or row == len(matrix) or col < 0 or col == len(matrix[0]):
        return
    if matrix[row][col] > 0:
        matrix[row][col] -= damage


n = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]
bombs = input().split(' ')
for i in bombs:
    row, col = [int(x) for x in i.split(',')]
    if matrix[row][col] > 0:
        damage = matrix[row][col]
        matrix[row][col] = 0
        decrease(matrix, damage, row - 1, col)
        decrease(matrix, damage, row - 1, col + 1)
        decrease(matrix, damage, row, col + 1)
        decrease(matrix, damage, row + 1, col + 1)
        decrease(matrix, damage, row + 1, col)
        decrease(matrix, damage, row + 1, col - 1)
        decrease(matrix, damage, row, col - 1)
        decrease(matrix, damage, row - 1, col - 1)
suma = 0
active = 0
for i in matrix:
    for j in i:
        if j > 0:
            suma += j
            active += 1
print(f'Alive cells: {active}')
print(f'Sum: {suma}')
for i in matrix:
    print(*i, sep=' ')
