a = input().lower().split(' ')
lst = []
for i in a:
    if a.count(i) % 2 != 0 and i not in lst:
        lst.append(i)
print(' '.join(lst))
