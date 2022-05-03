import math
n = int(input())
print('%' * (2 * n))
red = math.ceil(n / 2)
space = 2 * n - 2
for i in range(1, red):
	print('%' + ' ' * space + '%')
space_sred = n - 2
print('%' + ' ' * space_sred + '**' + ' ' * space_sred + '%')
for i in range(1, red):
	print('%' + ' ' * space + '%')
print('%' * (2 * n))
