import math
n = int(input())
tochki = n // 2
print('{0}{1}{0}'.format('.' * tochki, '#' * n))
tochki_mid = n - 2
for i in range(n - 2):
    print('{0}#{1}#{0}'.format('.' * tochki, '.' * tochki_mid))
dz_sred = math.ceil((n + 1) / 2)
print('{0}{1}{0}'.format('#' * dz_sred, '.' * tochki_mid))
tochkaotstrani = 1
sredna_tochka = 2 * n - 5
for x in range(n - 2):
    print('{0}#{1}#{0}'.format('.' * tochkaotstrani, '.' * sredna_tochka))
    sredna_tochka -= 2
    tochkaotstrani += 1
tochkadolu = n - 1
print('{0}#{0}'.format('.' * tochkadolu))
