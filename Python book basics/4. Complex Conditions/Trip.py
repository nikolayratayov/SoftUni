pari = float(input())
sezon = input().lower()
if pari <= 100:
    dest = 'Bulgaria'
    if sezon == 'summer':
        pochivka = 'Camp'
        spend = pari * 0.3
    elif sezon == 'winter':
        pochivka = 'Hotel'
        spend = pari * 0.7
elif 100 < pari <= 1000:
    dest = 'Balkans'
    if sezon == 'summer':
        pochivka = 'Camp'
        spend = pari * 0.4
    elif sezon == 'winter':
        pochivka = 'Hotel'
        spend = pari * 0.8
else:
    dest = 'Europe'
    spend = pari*0.9
    pochivka = 'Hotel'
spend = '{:.2f}'.format(spend)
print(f'Somewhere in {dest}')
print(f'{pochivka} - {spend}')
