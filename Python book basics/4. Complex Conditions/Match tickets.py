pari = float(input())
a = input().lower()
hora = int(input())
if 1 <= hora <= 4:
    pari = pari - (pari * 0.75)
elif 5 <= hora <= 9:
    pari = pari - (pari * 0.6)
elif 10 <= hora <= 24:
    pari = pari - (pari * 0.5)
elif 25 <= hora <= 49:
    pari = pari - (pari * 0.4)
elif hora >= 50:
    pari = pari - (pari * 0.25)
if a == 'vip':
    neobh_pari = hora * 499.99
elif a == 'normal':
    neobh_pari = hora * 249.99
if pari >= neobh_pari:
    razlika = pari - neobh_pari
    razlika = '{:.2f}'.format(razlika)
    print(f'Yes! You have {razlika} leva left.')
else:
    razlika = neobh_pari - pari
    razlika = '{:.2f}'.format(razlika)
    print(f'Not enough money! You need {razlika} leva.')
