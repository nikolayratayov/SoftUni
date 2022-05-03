def triangle(a):
    for i in range(1, a + 1):
        for j in range(1, i + 1):
            print(f'{j}', end=' ')
        print()
    for i in range(a, 0, -1):
        for j in range(1, i):
            print(f'{j}', end=' ')
        print()


a = int(input())
triangle(a)
