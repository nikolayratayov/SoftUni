i = int(input())
lekari = 7
pregledani = 0
nepregledani = 0
for i in range(1, i + 1):
    broi = int(input())
    if i % 3 == 0 and nepregledani > pregledani:
        lekari += 1
    if broi <= lekari:
        pregledani += broi
    else:
        pacient_ne = broi - lekari
        nepregledani += pacient_ne
        pregledani += lekari
print(f'Treated patients: {pregledani}.')
print(f'Untreated patients: {nepregledani}.')
