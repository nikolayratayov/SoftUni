a = input()
tempstr = ''
finalstr = ''
index = -1
digits = ''
for i in a:
    index += 1
    if not i.isdigit():
        tempstr += i.upper()
    else:
        digits += i
        if (index + 1) < len(a) and a[index + 1].isdigit():
            continue
        number = int(digits)
        finalstr += tempstr * number
        tempstr = ''
        digits = ''

unique = ''
for i in finalstr:
    if i not in unique:
        unique += i

print(f'Unique symbols used: {len(unique)}')
print(finalstr)
