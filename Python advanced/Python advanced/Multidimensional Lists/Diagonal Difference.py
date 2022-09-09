n = int(input())
matrix = [[int(x) for x in input().split(' ')] for _ in range(n)]
primary = 0
secondary = 0
for i in range(n):
    primary += matrix[i][i]
    secondary += matrix[n - 1 - i][i]
print(abs(primary - secondary))
