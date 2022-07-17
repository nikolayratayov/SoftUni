a = [int(x) for x in input().split(' ')]
is_sorted = False
while not is_sorted:
    is_sorted = True
    counter = 0
    for i in range(1, len(a) - counter):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            is_sorted = False
    counter += 1

print(*a, sep=' ')
