a = input()
b = []
for j in range(len(a)):
    if ord('A') <= ord(a[j]) <= ord('Z'):
        b.append(j)

print(b)
