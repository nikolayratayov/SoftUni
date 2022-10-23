n = int(input())
racing_number = input()

matrix = []
kms = 0

for _ in range(n):
    matrix.append([x for x in input().split(' ')])

row = 0
col = 0
matrix[row][col] = 'C'
DFN = False

while True:
    dir = input()
    if dir == 'End':
        DFN = True
        break
    if dir == 'up':
        matrix[row][col] = '.'
        row -= 1
        if matrix[row][col] == 'T':
            matrix[row][col] = '.'
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 'T':
                        row = i
                        col = j
                        matrix[row][col] = 'C'
                        kms += 30
        elif matrix[row][col] == 'F':
            matrix[row][col] = 'C'
            kms += 10
            break
        else:
            matrix[row][col] = 'C'
            kms += 10
    elif dir == 'right':
        matrix[row][col] = '.'
        col += 1
        if matrix[row][col] == 'T':
            matrix[row][col] = '.'
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 'T':
                        row = i
                        col = j
                        matrix[row][col] = 'C'
                        kms += 30
        elif matrix[row][col] == 'F':
            matrix[row][col] = 'C'
            kms += 10
            break
        else:
            matrix[row][col] = 'C'
            kms += 10
    elif dir == 'down':
        matrix[row][col] = '.'
        row += 1
        if matrix[row][col] == 'T':
            matrix[row][col] = '.'
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 'T':
                        row = i
                        col = j
                        matrix[row][col] = 'C'
                        kms += 30
        elif matrix[row][col] == 'F':
            matrix[row][col] = 'C'
            kms += 10
            break
        else:
            matrix[row][col] = 'C'
            kms += 10
    elif dir == 'left':
        matrix[row][col] = '.'
        col -= 1
        if matrix[row][col] == 'T':
            matrix[row][col] = '.'
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 'T':
                        row = i
                        col = j
                        matrix[row][col] = 'C'
                        kms += 30
        elif matrix[row][col] == 'F':
            matrix[row][col] = 'C'
            kms += 10
            break
        else:
            matrix[row][col] = 'C'
            kms += 10
if DFN:
    print(f'Racing car {racing_number} DNF.')
else:
    print(f'Racing car {racing_number} finished the stage!')
print(f'Distance covered {kms} km.')
for i in matrix:
    print(''.join(i))
