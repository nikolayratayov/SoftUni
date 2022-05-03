a = input().lower()
r = int(input())
c = int(input())
n = r*c
if a == 'premiere':
    print('%.2f' % (n*12))
elif a == 'normal':
    print('%.2f' % (n*7.5))
elif a == 'discount':
    print('%.2f' % (n*5))
