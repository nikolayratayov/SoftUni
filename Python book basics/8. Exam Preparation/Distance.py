v = int(input())
a = int(input())
b = int(input())
c = int(input())
ah = a / 60
bh = b / 60
ch = c / 60
s = v * ah + 1.1 * v * bh + 0.95 * 1.1 * v * ch
print(f'{s:.2f}')
