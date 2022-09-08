rows = int(input())
matrix = [[int(x) for x in input().split(', ')] for i in range(rows)]
primary = 0
primary_el = []
secondary = 0
secondary_el = []
for i in range(rows):
    primary += matrix[i][i]
    primary_el.append(matrix[i][i])
    secondary += matrix[rows - 1 - i][i]
    secondary_el.append(matrix[rows - 1 - i][i])
print(f"Primary diagonal: {', '.join(str(x) for x in primary_el)}. Sum: {primary}")
print(f"Secondary diagonal: {', '.join(str(x) for x in reversed(secondary_el))}. Sum: {secondary}")
