a = input().split(', ')
b = []
indexi = []
for i in a:
    b.append(int(i))
index = -1
for i in b:
    index += 1
    if i % 2 == 0:
        indexi.append(index)

print(indexi)