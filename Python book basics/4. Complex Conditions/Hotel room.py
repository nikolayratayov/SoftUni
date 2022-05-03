mesec = input().lower()
broi = int(input())
studio_cena = 0
apart_cena = 0
if mesec == 'may' or mesec == 'october':
    studio_cena = broi * 50
    if 7 < broi <= 14:
        studio_cena = studio_cena - (studio_cena * 0.05)
    elif broi > 14:
        studio_cena = studio_cena - (studio_cena * 0.3)
    apart_cena = broi * 65
elif mesec == 'june' or mesec == 'september':
    studio_cena = broi * 75.2
    if broi > 14:
        studio_cena = studio_cena - (studio_cena * 0.2)
    apart_cena = broi * 68.7
elif mesec == 'july' or mesec == 'august':
    studio_cena = broi * 76
    apart_cena = broi * 77
if broi > 14:
    apart_cena = apart_cena - (apart_cena * 0.1)
apart_cena = '{:.2f}'.format(apart_cena)
studio_cena = '{:.2f}'.format(studio_cena)
print(f'Apartment: {apart_cena} lv.')
print(f'Studio: {studio_cena} lv.')
