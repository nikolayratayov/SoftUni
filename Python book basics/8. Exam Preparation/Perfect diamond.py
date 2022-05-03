n = int(input())
if n == 1:
	print('*')
elif n != 0:
	space = n - 1
	space_drug = n - 2
	zvz_dolna = 1
	print(' ' * space + '*')
	for i in range(n - 1):
		print(' ' * space_drug + '*-' * zvz_dolna + '*')
		space_drug -= 1
		zvz_dolna += 1
	space_dolu = 1
	zvz_dolna_dolu = n - 2
	for j in range(n - 2):
		print(' ' * space_dolu + '*-' * zvz_dolna_dolu + '*')
		space_dolu += 1
		zvz_dolna_dolu -= 1
	print(' ' * space + '*')
