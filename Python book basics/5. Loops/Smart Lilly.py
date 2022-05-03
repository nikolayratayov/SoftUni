i = int(input())
a = float(input())
b = int(input())
igrachki = 0
pari = 0
podarak = 0
broi_chetni_rd = 0
for i in range(1, i + 1):
    if i % 2 != 0:
        igrachki += 1
    else:
        broi_chetni_rd += 1
        podarak += 10
        pari += podarak
spest_pari = pari - broi_chetni_rd
pari_ot_igrachki = igrachki * b
spest = spest_pari + pari_ot_igrachki
razlika = abs(a - spest)
if spest >= a:
    print(f'Yes! {razlika:.2f}')
else:
    print(f'No! {razlika:.2f}')
