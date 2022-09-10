n = int(input())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split(' ')])
suma = 0
for i in range(n):
    suma += matrix[i][i]
print(suma)
