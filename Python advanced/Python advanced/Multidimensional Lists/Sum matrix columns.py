rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(' ')])
for col in range(cols):
    sum = 0
    for row in range(rows):
        sum += matrix[row][col]
    print(sum)
