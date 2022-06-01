a = input()
copiedstr = a
index = -1
go = False
count = 0
strength = 0
for i in a:
    index += 1
    if go:
        if i == '>':
            continue
        try:
            strength += int(i)
        except:
            pass
        temp = index - count
        copiedstr = copiedstr[:temp] + copiedstr[temp + 1:]
        count += 1
        strength -= 1
        if strength == 0:
            go = False
    if i == '>':
        go = True
print(copiedstr)
