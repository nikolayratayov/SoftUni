first = int(input())
second = int(input())
point = int(input())
if min(first, second) <= point <= max(second, first):
	print('in')
else:
	print('out')
if point >= max(second, first):
	a = max(second, first) - point
a = abs((second - point))
b = abs((first - point))
print(min(a, b))
