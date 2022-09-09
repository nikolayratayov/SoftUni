rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(x) for x in input().split(', ')])
new_matrix = []
for i in matrix:
    temp = []
    for j in i:
        if j % 2 == 0:
            temp.append(j)
    new_matrix.append(temp)
print(new_matrix)
