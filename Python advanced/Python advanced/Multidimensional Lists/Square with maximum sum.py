rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
suma = -99999999999
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1] > suma:
            suma = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            elements = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
print(f'{elements[0]} {elements[1]}')
print(f'{elements[2]} {elements[3]}')
print(suma)
