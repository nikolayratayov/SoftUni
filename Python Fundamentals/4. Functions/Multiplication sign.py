a = int(input())
b = int(input())
c = int(input())
res = a * b * c
if res < 0:
    print('negative')
elif res == 0:
    print('zero')
else:
    print('positive')