i = int(input())
p1 = 0
p2 = 0
p3 = 0
for i in range(1, i + 1):
    a = int(input())
    if a % 2 == 0:
        p1 += 1
    if a % 3 == 0:
        p2 += 1
    if a % 4 == 0:
        p3 += 1
p1 = p1 / i * 100
p2 = p2 / i * 100
p3 = p3 / i * 100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
