chislata = input().split(', ')
chisla = []
for i in chislata:
    chisla.append(int(i))
for i in chisla:
    if i == 0:
        chisla.append(i)
        chisla.pop(chisla.index(i))

print(chisla)