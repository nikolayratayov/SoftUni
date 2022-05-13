a = int(input())
broi = 0
for i in range(a):
    broi += 1
    print('*' * broi)
broi = a
for i in range(a - 1):
    broi -= 1
    print('*' * broi)

