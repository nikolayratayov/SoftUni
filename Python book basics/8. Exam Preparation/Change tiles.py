import math
pari = float(input())
wpod = float(input())
lpod = float(input())
atri = float(input())
htri = float(input())
cenaplochka = float(input())
maistor = float(input())
spod = lpod * wpod
splochka = atri * htri / 2
neobplochki = math.ceil(spod / splochka) + 5
neobpari = neobplochki * cenaplochka + maistor
if pari >= neobpari:
    ost = pari - neobpari
    print(f'{ost:.2f} lv left.')
else:
    nedost = neobpari - pari
    print(f'You\'ll need {nedost:.2f} lv more.')
