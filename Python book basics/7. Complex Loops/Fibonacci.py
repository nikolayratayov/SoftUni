n = int(input())
F1 = 0
F2 = 1
for i in range(1, n + 1):
    chislo = F1 + F2
    F1 = F2
    F2 = chislo
if n == 0:
    print(F2)
else:
    print(chislo)
