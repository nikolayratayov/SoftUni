import math
n = int(input())
stars = 1
if n % 2 == 0:
    stars += 1
roof_lenght = math.ceil(n / 2)
for i in range(0, roof_lenght):
    padding = (n - stars) // 2
    line = ('-' * padding + '*' * stars + '-' * padding)
    print(line)
    stars += 2
osnova = math.floor(n / 2)
for i in range(osnova):
    print('|' + '*' * (n - 2) + '|')
