chislo = input()
chislo_list = list(chislo)

bik = int(input())
krava = int(input())

nqma = True

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                bik_a = 0
                krava_a = 0
                bik_b = 0
                krava_b = 0
                bik_c = 0
                krava_c = 0
                bik_d = 0
                krava_d = 0

                if a == int(chislo_list[0]):
                    bik_a = 1
                if b == int(chislo_list[1]):
                    bik_b = 1
                if c == int(chislo_list[2]):
                    bik_c = 1
                if d == int(chislo_list[3]):
                    bik_d = 1

                if bik_a == 0:
                    if a == int(chislo_list[1]) and bik_b == 0:
                        krava_a = 1
                    elif a == int(chislo_list[2]) and bik_c == 0:
                        krava_a = 1
                    elif a == int(chislo_list[3]) and bik_d == 0:
                        krava_a = 1

                if bik_b == 0:
                    if b == int(chislo_list[0]) and bik_a == 0:
                        krava_b = 1
                    elif b == int(chislo_list[2]) and (a != int(chislo_list[2]) or bik_a == 1) and bik_c == 0:
                        krava_b = 1
                    elif b == int(chislo_list[3]) and (a != int(chislo_list[3]) or bik_a == 1) and bik_d == 0:
                        krava_b = 1

                if bik_c == 0:
                    if c == int(chislo_list[0]) and bik_a == 0 and (b != int(chislo_list[0]) or bik_b == 1):
                        krava_c = 1
                    elif c == int(chislo_list[1]) and bik_b == 0 and (a != int(chislo_list[1]) or bik_a == 1):
                        krava_c = 1
                    elif c == int(chislo_list[3]) and (a != int(chislo_list[3]) or bik_a == 1) and (b != int(chislo_list[3]) or bik_b == 1) and bik_d == 0:
                        krava_c = 1

                if bik_d == 0:
                    if d == int(chislo_list[0]) and bik_a == 0 and (b != int(chislo_list[0]) or bik_b == 1) and (c != int(chislo_list[0]) or bik_c == 1):
                        krava_d = 1
                    elif d == int(chislo_list[1]) and bik_b == 0 and (a != int(chislo_list[1]) or bik_a == 1) and (c != int(chislo_list[1]) or bik_c == 1):
                        krava_d = 1
                    elif d == int(chislo_list[2]) and bik_c == 0 and (a != int(chislo_list[2]) or bik_a == 1) and (b != int(chislo_list[2]) or bik_b == 1):
                        krava_d = 1

                bik_prov = bik_a + bik_b + bik_c + bik_d
                krava_prov = krava_a + krava_b + krava_c + krava_d

                if bik_prov == bik and krava_prov == krava:
                    print(f'{a}{b}{c}{d}', end=' ')
                    nqma = False

if nqma:
    print('No')
