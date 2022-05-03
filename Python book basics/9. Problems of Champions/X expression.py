def izraz_v_skobi():
    global symbol
    symbol = izraz.pop(0)
    global b
    b = int(symbol)
    while True:
        symbol = izraz.pop(0)
        vatre_a = symbol
        if vatre_a == ')':
            return b
        else:
            symbol = izraz.pop(0)
            if vatre_a == '+':
                chislo = int(symbol)
                b += chislo
            elif vatre_a == '-':
                chislo = int(symbol)
                b -= chislo
            elif vatre_a == '*':
                chislo = int(symbol)
                b *= chislo
            elif vatre_a == '/':
                chislo = int(symbol)
                b /= chislo

kraino = 0
neshtosi = input()
izraz = list(neshtosi)
symbol = izraz.pop(0)
try:
    kraino = int(symbol)
except:
    izraz_v_skobi()
    kraino += b
while True:
    symbol = izraz.pop(0)
    a = symbol
    if a == '=':
        print(f'{kraino:.2f}')
        break

    else:
        symbol = izraz.pop(0)
        if a == '+':
            try:
                b = int(symbol)
            except:
                izraz_v_skobi()
            kraino += b
        elif a == '-':
            try:
                b = int(symbol)
            except:
                izraz_v_skobi()
            kraino -= b
        elif a == '*':
            try:
                b = int(symbol)
            except:
                izraz_v_skobi()
            kraino *= b
        elif a == '/':
            try:
                b = int(symbol)
            except:
                izraz_v_skobi()
            kraino /= b

