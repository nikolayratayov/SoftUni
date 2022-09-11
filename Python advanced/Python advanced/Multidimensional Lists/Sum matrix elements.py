rows, cols = [int(x) for x in input().split(', ')]
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
suma = 0
for i in matrix:
    suma += sum(i)
print(suma)
print(matrix)
