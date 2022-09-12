rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
new_matrix = []
for i in matrix:
    for j in i:
        new_matrix.append(j)
print(new_matrix)
