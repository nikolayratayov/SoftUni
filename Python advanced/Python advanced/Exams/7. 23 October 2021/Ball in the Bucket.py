matrix = []
for _ in range(6):
    matrix.append([x for x in input().split(' ')])
points = 0
for _ in range(3):
    row, col = [int(x) for x in input().strip('(').rstrip(')').split(', ')]
    if row >= 6 or col >= 6:
        continue
    if matrix[row][col] == 'B':
        matrix[row][col] = 0
        for i in range(6):
            points += int(matrix[i][col])

if points < 100:
    print(f'Sorry! You need {100 - points} points more to win a prize.')
elif 100 <= points <= 199:
    print(f'Good job! You scored {points} points, and you\'ve won Football.')
elif 200 <= points <= 299:
    print(f'Good job! You scored {points} points, and you\'ve won Teddy Bear.')
else:
    print(f'Good job! You scored {points} points, and you\'ve won Lego Construction Set.')
