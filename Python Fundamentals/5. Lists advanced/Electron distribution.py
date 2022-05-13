n = int(input())
a = 0
shells = []
while True:
    a += 1
    trqbvat = 2 * a ** 2
    if trqbvat <= n:
        shells.append(trqbvat)
        n -= trqbvat
    else:
        shells.append(n)
        break
    if n == 0:
        break

print(shells)