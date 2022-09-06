n = int(input())
odd_set = set()
even_set = set()
for i in range(1, n + 1):
    name = input()
    num = 0
    for j in name:
        num += ord(j)
    num //= i
    if num % 2 == 0:
        even_set.add(num)
    else:
        odd_set.add(num)

if sum(odd_set) == sum(even_set):
    res_set = odd_set.union(even_set)
elif sum(odd_set) > sum(even_set):
    res_set = odd_set.difference(even_set)
else:
    res_set = odd_set.symmetric_difference(even_set)
print(*res_set, sep=', ')
