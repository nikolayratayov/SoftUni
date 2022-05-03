a = float(input())
b = input()
if b == 'm' and a >= 16:
    print('Mr.')
elif b == 'm' and a < 16:
    print('Master')
elif b == 'f':
    if a >= 16:
        print('Ms.')
    else:
        print('Miss')
