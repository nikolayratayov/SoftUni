a = input().split(' ')
nov = []
for i in a:
    sym = ''
    for j in i:
        if 48 <= ord(j) <= 57:
            sym += j
    sym = int(sym)
    if sym < 100:
        duma = chr(sym) + i[2:]
        nov.append(duma)
    else:
        duma = chr(sym) + i[3:]
        nov.append(duma)
# print(nov)
pakdr = []
for i in nov:
    if len(i) > 2:
        last = i[len(i) - 1]
        second = i[1]
        dumata = i[:1] + last + i[2:len(i) - 1] + second
        pakdr.append(dumata)
    else:
        pakdr.append(i)
count = 0
for i in pakdr:
    count += 1
    if count == len(pakdr):
        print(i)
        break
    print(i, end=' ')