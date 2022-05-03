n = int(input())
for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				for e in range(1, 10):
					for f in range(1, 10):
						if a * b * c * d * e * f == n:
							print(f'{a}{b}{c}{d}{e}{f}', end=' ')
