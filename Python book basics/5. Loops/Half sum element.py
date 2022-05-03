import math
i = int(input())
summ = 0
maxx = -999999999999
for i in range(0, i):
    a = int(input())
    summ += a
    if a > maxx:
        maxx = a
suma_bez_max = summ - maxx
razlika = math.fabs(suma_bez_max - maxx)
if suma_bez_max == maxx:
    print('Yes')
    print(f'Sum = {str(suma_bez_max)}')
else:
    print('No')
    print(f'Diff = {str(razlika)}')
