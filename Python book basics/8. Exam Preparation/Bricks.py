import math
tuhli = int(input())
rabotnici = int(input())
kurs = int(input())
pone = math.ceil(tuhli / (rabotnici * kurs))
print(pone)
