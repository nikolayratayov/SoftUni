vhod = input().split(' ')
a = vhod[0]
b = vhod[1]
suma = 0
if len(a) > len(b):
    broi = len(b)
else:
    broi = len(a)
index = -1
for i in range(0, broi):
    index += 1
    suma += ord(a[index]) * ord(b[index])

if len(a) > len(b):
    for i in range(index + 1, len(a)):
        suma += ord(a[i])
elif len(b) > len(a):
    for i in range(index + 1, len(b)):
        suma += ord(b[i])
print(suma)
