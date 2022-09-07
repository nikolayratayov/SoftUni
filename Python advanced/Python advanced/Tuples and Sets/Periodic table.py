n = int(input())
el = set()
for i in range(n):
    eee = [x for x in input().split(' ')]
    for j in eee:
        el.add(j)
print('\n'.join(el))
