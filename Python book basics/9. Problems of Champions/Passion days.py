import decimal
decimal.getcontext().prec = 10000
pari = decimal.Decimal(input())
while True:
    basi = input()
    if basi == 'mall.Enter':
        break

pokupki = 0
while True:
    deistvie = input()
    if deistvie == 'mall.Exit':
        break
    for i in deistvie:
        if ord(i) in range(ord('A'), ord('Z') + 1):
            minus = decimal.Decimal(round((0.5 * ord(i)), 2))
            if minus > pari:
                continue
            pokupki += 1
            pari -= minus
        elif ord(i) in range(ord('a'), ord('z') + 1):
            minus = decimal.Decimal(round((0.3 * ord(i)), 2))
            if minus > pari:
                continue
            pokupki += 1
            pari -= minus
        elif i == '%' and pari > 0:
            pokupki += 1
            minus = decimal.Decimal(round((pari * decimal.Decimal(0.5)), 2))
            pari -= minus
        elif i == '*':
            pari += decimal.Decimal(10)
        else:
            minus = decimal.Decimal(ord(i))
            if minus > pari:
                continue
            pari -= minus
            pokupki += 1

if pokupki > 0:
    print(f'{pokupki} purchases. Money left: {pari:.2f} lv.')
else:
    print(f'No purchases. Money left: {pari:.2f} lv.')
