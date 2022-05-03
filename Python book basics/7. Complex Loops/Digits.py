a = int(input())
parva = a // 100
vtora = (a // 10) % 10
treta = a % 10
for i in range(1, parva + vtora + 1):
	for x in range(1, parva + treta + 1):
		if a % 5 == 0:
			a = a - parva
			print(a, end=' ')
		elif a % 3 == 0:
			a = a - vtora
			print(a, end=' ')
		else:
			a = a + treta
			print(a, end=' ')
	print()
