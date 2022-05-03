n = int(input())
dolna_lqvo = n * 3
dolna_dqsno = n * 2 - 2
print('{0}**{1}'.format('-' * dolna_lqvo, '-' * dolna_dqsno))
dolna_sreda = 1
dolna_dqsno = n * 2 - 3
for i in range(n - 1):
    print('{0}*{1}*{2}'.format('-' * dolna_lqvo, '-' * dolna_sreda, '-' * dolna_dqsno))
    dolna_sreda += 1
    dolna_dqsno -= 1
for i in range(n // 2):
    print('{0}*{1}*{1}'.format('*' * dolna_lqvo, '-' * (n - 1)))
a = n * 3
b = n - 1
c = n - 1
for i in range((n // 2) - 1):
    print('{0}*{1}*{2}'.format('-' * a, '-' * b, '-' * c))
    a -= 1
    c -= 1
    b += 2
print('{0}*{1}*{2}'.format('-' * a, '*' * b, '-' * c))
