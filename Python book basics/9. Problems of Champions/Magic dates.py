import datetime
nachgod = int(input())
kraigod = int(input())
teglo = int(input())
start = datetime.date(nachgod, 1, 1)
krai = datetime.date(kraigod + 1, 1, 1)
dni = krai - start
a = dni.days
ima = False
for i in range(a):
    b = start.day
    c = start.month
    if b < 10:
        parva = 0
        vtora = b
    else:
        parva = b // 10
        vtora = b % 10
    if c < 10:
        treta = 0
        chetv = c
    else:
        treta = c // 10
        chetv = c % 10
    d = start.year
    peta = d // 1000
    shesta = (d // 100) % 10
    sedma = (d // 10) % 10
    osma = d % 10
    tapototeglo = parva * (vtora + treta + chetv + peta + shesta + sedma + osma) +\
        vtora * (treta + chetv + peta + shesta + sedma + osma) + \
        treta * (chetv + peta + shesta + sedma + osma) +\
        chetv * (peta + shesta + sedma + osma) +\
        peta * (shesta + sedma + osma) +\
        shesta * (sedma + osma) +\
        sedma * osma
    if tapototeglo == teglo:
        dennn = start.strftime('%d')
        meseccc = start.strftime('%m')
        godina = start.strftime('%Y')
        print(f'{dennn}-{meseccc}-{godina}')
        ima = True
    start += datetime.timedelta(days=1)
if not ima:
    print('No')
