a = int(input())
b = int(input())
c = int(input())
if a + b == c:
	print(f'{min(a, b)} + {max(a, b)} = {c}')
elif a + c == b:
	print(f'{min(a, c)} + {max(a, c)} = {b}')
elif b + c == a:
	print(f'{min(b, c)} + {max(b, c)} = {a}')
else:
	print('No')
