n = int(input())
a = 1
end = False
for i in range(1, n + 1):
    if not end:
        for j in range(1, i + 1):
            print(a, end=' ')
            if a == n:
                end = True
                break
            a += 1
        print()
