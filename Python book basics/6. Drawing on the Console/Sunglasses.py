n = int(input())
red = '*' * 2 * n + ' ' * n + '*' * 2 * n
spaces = ' ' * n
prava = '|' * n
print(red)
for i in range(1, n - 1):
    print('*' + '/' * (n - 1) * 2 + '*', end='')
    usl = (n - 1) // 2
    if i == usl:
        print(prava, end='')
    else:
        print(spaces, end='')
    print('*' + '/' * (n - 1) * 2 + '*')
print(red)
