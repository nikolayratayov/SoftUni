n, m = [int(x) for x in input().split(' ')]
n_set = set()
m_set = set()
for i in range(n):
    n_set.add(int(input()))
for i in range(m):
    m_set.add(int(input()))

res = n_set.intersection(m_set)
print(*res, sep='\n')
