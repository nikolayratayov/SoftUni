n = int(input())
sum1 = 0
sum2 = 0
sum3 = 0
for i in range(1, n + 1):
	a = int(input())
	if i in range(1, n + 1, 3):
		sum1 += a
	elif i in range(2, n + 1, 3):
		sum2 += a
	elif i in range(3, n+1, 3):
		sum3 += a
print(f'sum1 = {sum1}')
print(f'sum2 = {sum2}')
print(f'sum3 = {sum3}')
