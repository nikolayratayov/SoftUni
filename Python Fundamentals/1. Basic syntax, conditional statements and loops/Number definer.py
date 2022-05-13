a = float(input())

if a == 0:
    print('zero')
elif 0 < a < 1:
    print('small positive')
elif 1 <= a < 1000000:
    print('positive')
elif a >= 1000000:
    print('large positive')
elif 0 > a > -1:
    print('small negative')
elif -1 >= a > -1000000:
    print('negative')
else:
    print('large negative')
