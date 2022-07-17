a = [int(x) for x in input().split(' ')]

for i in range(len(a)):
    new_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[new_idx]:
            new_idx = j
    a[i], a[new_idx] = a[new_idx], a[i]

print(*a, sep=' ')
