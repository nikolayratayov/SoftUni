import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
x3 = int(x3)
y3 = int(y3)
x4 = int(x4)
y4 = int(y4)


def longer(x1, y1, x2, y2, x3, y3, x4, y4):
    first = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    second = math.sqrt((x3 - x4) ** 2 + (y3 - y4) ** 2)
    if first >= second:
        p1 = math.sqrt(x1 * x1 + y1 * y1)
        p2 = math.sqrt(x2 * x2 + y2 * y2)
        if p1 <= p2:
            print(f'({x1}, {y1})({x2}, {y2})')
        else:
            print(f'({x2}, {y2})({x1}, {y1})')
    else:
        p1 = math.sqrt(x3 * x3 + y3 * y3)
        p2 = math.sqrt(x4 * x4 + y4 * y4)
        if p1 <= p2:
            print(f'({x3}, {y3})({x4}, {y4})')
        else:
            print(f'({x4}, {y4})({x3}, {y3})')


longer(x1, y1, x2, y2, x3, y3, x4, y4)
