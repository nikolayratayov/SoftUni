n = int(input())
shir = 4 * n + 1
vis = 2 * n + 5
tochki = int((shir - 3) / 2)
tere = 0
print('.' * tochki + '/|\\' + '.' * tochki)
print('.' * tochki + '\\|/' + '.' * tochki)
for i in range(2 * n):
    print('.' * tochki + '*' + '-' * tere + '*' + '-' * tere + '*' + '.' * tochki)
    tochki -= 1
    tere += 1
print('*' * shir)
print('*' + '.*' * n + '.*' * n)
print('*' * shir)
