def crypt(symbol):
    global niz
    niz = ''
    symbol = str(ord(symbol))
    parva = symbol[0]
    posl = symbol[(len(symbol) - 1)]
    niz = niz + parva + posl
    sbor = int(symbol) + int(posl)
    sbor = chr(sbor)
    niz = sbor + niz
    razlika = int(symbol) - int(parva)
    razlika = chr(razlika)
    niz = niz + razlika
    return niz


niz = ''
aha = ''
n = int(input())
for i in range(n):
    symbol = input()
    crypt(symbol)
    aha += niz
print(aha)
