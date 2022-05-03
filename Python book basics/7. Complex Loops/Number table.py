n = int(input())
for i in range(n):
    for j in range(n):
        a = i + j + 1
        if a > n:
            a = 2 * n - a
        print(f'{a} ', end='')
    print()
