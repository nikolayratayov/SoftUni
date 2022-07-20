def find_area(i, j, matrix, symbol):
    if i < 0 or j < 0 or i == n or j == m:
        return
    if symbol != matrix[i][j]:
        return
    matrix[i][j] = True
    find_area(i, j - 1, matrix, symbol)
    find_area(i - 1, j, matrix, symbol)
    find_area(i, j + 1, matrix, symbol)
    find_area(i + 1, j, matrix, symbol)


n = int(input())
m = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))

results = {}
areas = 0

for i in range(n):
    for j in range(m):
        haha = matrix[i][j]
        if matrix[i][j] == True:
            continue
        find_area(i, j, matrix, matrix[i][j])
        if haha not in results:
            results[haha] = 1
        else:
            results[haha] += 1
        areas += 1
print(f'Areas: {areas}')
for k, v in sorted(results.items()):
    print(f'Letter \'{k}\' -> {v}')
