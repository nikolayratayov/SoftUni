n = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'B':
            start_row = row
            start_col = col
up = []
right = []
down = []
left = []
total_eggs = []

max_eggs = float('-inf')
eggs = 0
for i in range(start_row - 1, -1, -1):
    if matrix[i][start_col] == 'X':
        break
    up.append([i, start_col])
    eggs += int(matrix[i][start_col])
    if eggs > max_eggs:
        max_eggs = eggs
        idx = 0

eggs = 0
for i in range(start_col + 1, n):
    if matrix[start_row][i] == 'X':
        break
    right.append([start_row, i])
    eggs += int(matrix[start_row][i])
    if eggs > max_eggs:
        max_eggs = eggs
        idx = 1

eggs = 0
for i in range(start_row + 1, n):
    if matrix[i][start_col] == 'X':
        break
    down.append([i, start_col])
    eggs += int(matrix[i][start_col])
    if eggs > max_eggs:
        max_eggs = eggs
        idx = 2

eggs = 0
for i in range(start_col - 1, -1, -1):
    if matrix[start_row][i] == 'X':
        break
    left.append([start_row, i])
    eggs += int(matrix[start_row][i])
    if eggs > max_eggs:
        max_eggs = eggs
        idx = 3

if idx == 0:
    print('up')
    for i in up:
        print(i)
elif idx == 1:
    print('right')
    for i in right:
        print(i)
elif idx == 2:
    print('down')
    for i in down:
        print(i)
elif idx == 3:
    print('left')
    for i in left:
        print(i)
print(max_eggs)
