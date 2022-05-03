chas = int(input())
minuti = int(input())
minuti += 15
if minuti >= 60:
    chas_plus = minuti // 60
    minuti = minuti % 60
    chas += chas_plus
    if chas >= 24:
        chas = chas % 24
        if minuti >= 10:
            print(f'{chas}:{minuti}')
        else:
            print(f'{chas}:0{minuti}')
    else:
        if minuti >= 10:
            print(f'{chas}:{minuti}')
        else:
            print(f'{chas}:0{minuti}')
else:
    print(f'{chas}:{minuti}')
