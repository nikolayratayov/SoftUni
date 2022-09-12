rows, cols = [int(x) for x in input().split(' ')]
snake = input()
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
idx = -1
start = 0
end = cols
step = 1
for row in range(rows):
    for col in range(start, end, step):
        idx += 1
        if idx == len(snake):
            idx = 0
        matrix[row][col] = snake[idx]
        if col == end - 1 and step == 1:
            step = -1
            start = end - 1
            end = -1
        elif col == 0 and step == -1:
            step = 1
            start = 0
            end = cols
for i in matrix:
    print(''.join(i))
