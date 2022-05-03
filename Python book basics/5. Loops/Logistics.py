i = int(input())
bus = 0
kamion = 0
vlak = 0
summ = 0
for i in range(1, i + 1):
    a = int(input())
    summ += a
    if a <= 3:
        bus += a
    elif 3 < a <= 11:
        kamion += a
    elif a > 11:
        vlak += a
pbus = bus / summ * 100
pkamion = kamion / summ * 100
pvlak = vlak / summ * 100
sr_cena = (bus * 200 + kamion * 175 + vlak * 120) / summ
print(f'{sr_cena:.2f}')
print(f'{pbus:.2f}%')
print(f'{pkamion:.2f}%')
print(f'{pvlak:.2f}%')
