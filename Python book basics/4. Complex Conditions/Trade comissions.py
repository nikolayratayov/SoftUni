a = (input().lower())
b = float(input())
com = -1
if a == 'sofia':
    if 0 <= b <= 500:
        com = 0.05
    elif 500 < b <= 1000:
        com = 0.07
    elif 1000 < b <= 10000:
        com = 0.08
    elif b > 10000:
        com = 0.12
elif a == 'plovdiv':
    if 0 <= b <= 500:
        com = 0.055
    elif 500 < b <= 1000:
        com = 0.08
    elif 1000 < b <= 10000:
        com = 0.12
    elif b > 10000:
        com = 0.145
elif a == 'varna':
    if 0 <= b <= 500:
        com = 0.045
    elif 500 < b <= 1000:
        com = 0.075
    elif 1000 < b <= 10000:
        com = 0.1
    elif b > 10000:
        com = 0.13
if com >= 0:
    print('%.2f' % (b*com))
else:
    print('error')
