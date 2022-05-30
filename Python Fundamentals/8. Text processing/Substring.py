a = input()
b = input()
while True:
    if a in b:
        b = b.replace(a, '')
    else:
        break
print(b)