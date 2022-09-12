n = int(input())
matrix = [[x for x in input().split(' ')] for _ in range(n)]
tea = 0
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'A':
            row = i
            col = j
matrix[row][col] = '*'
while True:
    command = input()
    if command == 'up':
        row -= 1
        if row == -1:
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == '.' or matrix[row][col] == '*':
            matrix[row][col] = '*'
            continue
        tea += int(matrix[row][col])
        matrix[row][col] = '*'
        if tea >= 10:
            print('She did it! She went to the party.')
            break
    elif command == 'right':
        col += 1
        if col == n:
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == '.' or matrix[row][col] == '*':
            matrix[row][col] = '*'
            continue
        tea += int(matrix[row][col])
        matrix[row][col] = '*'
        if tea >= 10:
            print('She did it! She went to the party.')
            break
    elif command == 'down':
        row += 1
        if row == n:
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == '.' or matrix[row][col] == '*':
            matrix[row][col] = '*'
            continue
        tea += int(matrix[row][col])
        matrix[row][col] = '*'
        if tea >= 10:
            print('She did it! She went to the party.')
            break
    elif command == 'left':
        col -= 1
        if col == -1:
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == 'R':
            matrix[row][col] = '*'
            print(f'Alice didn\'t make it to the tea party.')
            break
        if matrix[row][col] == '.' or matrix[row][col] == '*':
            matrix[row][col] = '*'
            continue
        tea += int(matrix[row][col])
        matrix[row][col] = '*'
        if tea >= 10:
            print('She did it! She went to the party.')
            break
for i in matrix:
    print(' '.join(i))
