a = int(input())
field = []
for i in range(a):
    b = input().split(' ')
    eee = []
    for j in b:
        eee.append(int(j))
    field.append(eee)

nachbr = 0
for i in field:
    for j in i:
        if j > 0:
            nachbr += 1

c = input().split(' ')
attack = []
for i in c:
    d = i.split('-')
    attack.append(d)

for i in attack:
    row = int(i[0])
    col = int(i[1])
    ship = field[row][col]
    ship -= 1
    field[row][col] = ship

kraibr = 0
for i in field:
    for j in i:
        if j > 0:
            kraibr += 1

print(nachbr - kraibr)
