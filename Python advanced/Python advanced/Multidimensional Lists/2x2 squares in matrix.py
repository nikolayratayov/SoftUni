rows, cols = [int(x) for x in input().split(' ')]
matrix = [[x for x in input().split(' ')] for _ in range(rows)]
equals = 0
for row in range(rows - 1):
    for col in range(cols - 1):
        if matrix[row][col] == matrix[row][col + 1] and matrix[row][col] == matrix[row + 1][col] and matrix[row][col] == matrix[row + 1][col +1]:
            equals += 1
print(equals)
