a = float(input())
i = int(input())
parichet = 0
parinechet = 0
god = -1
for i in range(1800, i + 1):
    god += 1
    if i % 2 == 0:
        parichet += 12000
    else:
        parinechet = parinechet + 12000 + 50 * (god + 18)
pari = parichet + parinechet
razlika = abs(a - pari)
if a >= pari:
    print(f'Yes! He will live a carefree life and will have {razlika:.2f} dollars left.')
else:
    print(f'He will need {razlika:.2f} dollars to survive.')
