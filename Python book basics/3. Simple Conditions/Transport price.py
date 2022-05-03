a = int(input())
b = input()
taxi_nach = 0.7
taxi_den = 0.79
taxi_nosht = 0.9
avt = 0.09
vlak = 0.06
if a >= 100:
    print(a*vlak)
elif 20 <= a < 100:
    print(a*avt)
else:
    if b == 'day':
        print(a*taxi_den+taxi_nach)
    elif b == 'night':
        print(a*taxi_nosht+taxi_nach)
