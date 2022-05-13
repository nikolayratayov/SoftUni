n = int(input())

for i in range(1, n + 1):
    dali = False
    suma = 0
    for j in str(i):
        suma += int(j)
    if suma == 5 or suma == 7 or suma == 11:
        dali = True
    print(f'{i} -> {dali}')