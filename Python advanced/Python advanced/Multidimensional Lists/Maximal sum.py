rows, cols = [int(x) for x in input().split(' ')]
matrix = [[int(x) for x in input().split(' ')] for _ in range(rows)]
max_sum = -999999999999
for row in range(rows - 2):
    for col in range(cols - 2):
        suma = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + \
              matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + \
              matrix[row + 2][col + 2]
        if suma > max_sum:
            max_sum = suma
            els = [[matrix[row][col], matrix[row][col + 1], matrix[row][col + 2]], [matrix[row + 1][col],
              matrix[row + 1][col + 1], matrix[row + 1][col + 2]], [matrix[row + 2][col], matrix[row + 2][col + 1],
              matrix[row + 2][col + 2]]]
print(f'Sum = {max_sum}')
for i in els:
    print(*i, sep=' ')
