i = int(input())
broip1 = 0
broip2 = 0
broip3 = 0
broip4 = 0
broip5 = 0
summ = 0
for i in range(1, i+1):
    a = int(input())
    if a < 200:
        broip1 += 1
    elif 200 <= a <= 399:
        broip2 += 1
    elif 400 <= a <= 599:
        broip3 += 1
    elif 600 <= a <= 799:
        broip4 += 1
    elif a >= 800:
        broip5 += 1
p1 = broip1 / i * 100
p2 = broip2 / i * 100
p3 = broip3 / i * 100
p4 = broip4 / i * 100
p5 = broip5 / i * 100
print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
