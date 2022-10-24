n = int(input())

if n == 1:
    print('*')
else:
    for i in range(1, n):
        print(' ' * (n - i - 1) + ' *' * i)
    print('*' + ' *' * (n - 1))
    for i in range(n - 1, 0, -1):
        print(' ' * (n - i - 1) + ' *' * i)
