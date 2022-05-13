n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print('1 1')
elif n == 3:
    print('1 1 2')
else:
    print('1 1 2 ', end='')
    parva = 1
    vtora = 1
    treta = 2
    for i in range(n - 3):
        chislo = parva + vtora + treta
        print(f'{chislo}', end=' ')
        parva = vtora
        vtora = treta
        treta = chislo


