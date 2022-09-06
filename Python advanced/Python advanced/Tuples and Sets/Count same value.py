lst = [float(x) for x in input().split(' ')]
items = []
counts = []
for i in lst:
    counter = 0
    if i not in items:
        for j in lst:
            if i == j:
               counter += 1
        items.append(i)
        counts.append(counter)

for i in range(len(items)):
    print(f'{items[i]} - {counts[i]} times')
