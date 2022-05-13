import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x1 = math.floor(x1)
y1 = math.floor(y1)
x2 = math.floor(x2)
y2 = math.floor(y2)

def closest(a, b, c, d):
    p1 = math.sqrt(a * a + b * b)
    p2 = math.sqrt(c * c + d * d)
    if p1 <= p2:
        return int(a), int(b)
    else:
        return int(c), int(d)


print(f'{(closest(x1, y1, x2, y2))}')