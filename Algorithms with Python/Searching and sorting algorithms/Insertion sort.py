a = [int(x) for x in input().split(' ')]
i = 0
j = 1
while True:
    if j == len(a):
        break
    if a[j] < a[i]:
        a[j], a[i] = a[i], a[j]
        if i == 0:
            i = 0
            j = 1
        else:
            i -= 1
            j -= 1
    else:
        i += 1
        j += 1

print(*a, sep=' ')
