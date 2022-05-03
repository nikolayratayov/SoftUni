i = int(input())
x = 0
y = 0
razlika_kraina = 0
razlika = -99999999999
for i in range(1, i + 1):
    summ1 = x
    a = int(input())
    b = int(input())
    summ2 = a + b
    if summ2 - summ1 != 0:
        x = summ2
        if i != 1:
            b = razlika
            razlika = abs(summ2 - summ1)
            if razlika > b:
                razlika_kraina = razlika
if razlika_kraina == 0:
    print(f'Yes, value={summ2}')
else:
    print(f'No, maxdiff={razlika_kraina}')
