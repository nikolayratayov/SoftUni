n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
symbol = input()
nqma = True
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symbol and nqma:
            print(f'({row}, {col})')
            nqma = False
if nqma:
    print(f'{symbol} does not occur in the matrix')
