n = int(input())
tochki = n + 1
dolna = 2 * n + 1
print('{0}{1}{0}'.format('.' * tochki, '_' * dolna))
tochki -= 1
dolna -= 2
for i in range(n):
    print('{0}//{1}\\\\{0}'.format('.' * tochki, '_' * dolna))
    dolna += 2
    tochki -= 1
print('//{0}STOP!{0}\\\\'.format('_' * ((dolna - 5) // 2)))
for i in range(n):
    print('{0}\\\\{1}//{0}'.format('.' * i, '_' * dolna))
    dolna -= 2
