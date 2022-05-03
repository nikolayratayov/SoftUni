n = int(input())
for row in range(1, n + 1):
    for col in range(1, n - row + 1):
        print(' ', end='')
    print('*', end='')
    for col in range(1, row):
        print(' *', end='')
    print()
for row in range(0, n - 1):
    print(' ' * row, end='')
    for col in range(0, n - row - 1):
        print(' *', end='')
    print()
