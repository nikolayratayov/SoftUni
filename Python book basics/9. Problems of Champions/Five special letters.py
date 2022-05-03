nach = int(input())
krai = int(input())
listtt = []
eho = True

for i in range(ord('a'), ord('e') + 1):
    for j in range(ord('a'), ord('e') + 1):
        for k in range(ord('a'), ord('e') + 1):
            for l in range(ord('a'), ord('e') + 1):
                for m in range(ord('a'), ord('e') + 1):
                    listtt.extend([chr(i), chr(j), chr(k), chr(l), chr(m)])
                    listtt = list(dict.fromkeys(listtt))
                    count = 0
                    parva = 0
                    vtora = 0
                    treta = 0
                    chetv = 0
                    peta = 0

                    for x in listtt:
                        count += 1

                        if x == 'a':
                            teglo = 5
                        elif x == 'b':
                            teglo = -12
                        elif x == 'c':
                            teglo = 47
                        elif x == 'd':
                            teglo = 7
                        elif x == 'e':
                            teglo = -32

                        if count == 1:
                            parva = teglo
                        elif count == 2:
                            vtora = teglo
                        elif count == 3:
                            treta = teglo
                        elif count == 4:
                            chetv = teglo
                        elif count == 5:
                            peta = teglo

                    formula = 1 * parva + 2 * vtora + 3 * treta + 4 * chetv + 5 * peta

                    if formula in range(nach, krai + 1):
                        print(f'{chr(i)}{chr(j)}{chr(k)}{chr(l)}{chr(m)}', end=' ')
                        eho = False
                    listtt = []
if eho:
    print('No')
