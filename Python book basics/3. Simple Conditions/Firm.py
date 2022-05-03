import math
neob_chas = int(input())
dni = int(input())
rabotnici = int(input())
dni_ostav = dni-0.1*dni
rab_chas = math.floor(dni_ostav*10*rabotnici)
if rab_chas >= neob_chas:
    ost_chas = rab_chas-neob_chas
    print(f'Yes!{ost_chas} hours left.')
else:
    ost_chas = neob_chas-rab_chas
    print(f'Not enough time!{ost_chas} hours needed.')
