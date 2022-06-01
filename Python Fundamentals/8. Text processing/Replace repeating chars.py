a = input()
old = ''
newstr = ''
for i in a:
    if old == i:
        old = i
        continue
    else:
        old = i
        newstr += i
print(newstr)
