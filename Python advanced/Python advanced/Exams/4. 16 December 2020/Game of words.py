def move(row, col, matrix):
    global current_col
    global current_row
    global word
    if row == -1 or row == n or col == -1 or col == n:
        word = word[:len(word) - 1]
        return
    matrix[current_row][current_col] = '-'
    if matrix[row][col] != '-':
        word += matrix[row][col]
    matrix[row][col] = 'P'
    current_row = row
    current_col = col
    return


word = input()
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
m = int(input())

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'P':
            current_row = i
            current_col = j

for _ in range(m):
    command = input()
    if command == 'left':
        move(current_row, current_col - 1, matrix)
    elif command == 'up':
        move(current_row - 1, current_col, matrix)
    elif command == 'right':
        move(current_row, current_col + 1, matrix)
    elif command == 'down':
        move(current_row + 1, current_col, matrix)
print(word)
for i in matrix:
    print(''.join(i))
