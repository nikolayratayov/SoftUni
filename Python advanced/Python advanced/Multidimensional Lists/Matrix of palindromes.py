rows, cols = [int(x) for x in input().split(' ')]
matrix = []
for row in range(rows):
    matrix.append([])
    for col in range(cols):
        word = chr(row + 97) + chr(row + col + 97) + chr(row + 97)
        matrix[row].append(word)
for i in matrix:
    print(' '.join(i))
