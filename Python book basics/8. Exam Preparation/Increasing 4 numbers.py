a = int(input())
b = int(input())
malko = min(a, b)
golqmo = max(a, b)
if golqmo - malko <= 2:
    print('No')
else:
    for i in range(malko, golqmo + 1):
        for j in range(i + 1, golqmo + 1):
            for k in range(j + 1, golqmo + 1):
                for l in range(k + 1, golqmo + 1):
                    print(f'{i} {j} {k} {l}')