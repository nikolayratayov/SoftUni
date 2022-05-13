n = int(input())
a = 255
tank = 0
for i in range(n):
    b = int(input())
    if b <= a:
        tank += b
        a -= b
    else:
        print('Insufficient capacity!')

print(tank)