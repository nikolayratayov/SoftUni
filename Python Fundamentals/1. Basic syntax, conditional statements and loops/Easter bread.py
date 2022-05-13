budjet = float(input())
cena_brashno_kg = float(input())
cena_qica = 0.75 * cena_brashno_kg
cena_mlqko = 1.25 * cena_brashno_kg / 4

broi_hlqb = 0
mlqko = 0
polucheni_qica = 0

while True:
    if budjet < cena_mlqko + cena_qica + cena_brashno_kg:
        break
    budjet -= cena_qica + cena_brashno_kg + cena_mlqko
    broi_hlqb += 1

    polucheni_qica += 3
    if broi_hlqb % 3 == 0:
        polucheni_qica -= broi_hlqb - 2

print(f'You made {broi_hlqb} loaves of Easter bread! Now you have {polucheni_qica} eggs and {budjet:.2f}BGN left.')
