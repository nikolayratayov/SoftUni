import math

a = input()
if a == 'square':
    b = float(input())
    s = b*b
elif a == 'rectangle':
    b = float(input())
    c = float(input())
    s = b*c
elif a == 'circle':
    b = float(input())
    s = math.pi*b*b
elif a == 'triangle':
    b = float(input())
    h = float(input())
    s = b*h/2
print(round(s, 3))
