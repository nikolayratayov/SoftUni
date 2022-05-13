n = int(input())
for i in range(n):
    a = input()
    if ',' in a or '.' in a or '_' in a:
        print(f'{a} is not pure!')
    else:
        print(f'{a} is pure.')

