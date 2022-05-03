n = int(input())
l = int(input())
for i in range(1, n + 1):
	for j in range(1, n + 1):
		for k in range(97, 97 + l):
			for m in range(97, 97 + l):
				for x in range(1, n + 1):
					if x > i and x > j:
						y = chr(k)
						z = chr(m)
						print(f'{i}{j}{y}{z}{x}', end=' ')
