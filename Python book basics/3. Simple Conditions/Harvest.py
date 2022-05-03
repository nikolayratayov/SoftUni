import math

a = int(input())
b = float(input())
c = int(input())
d = int(input())
vino = a*0.4*b/2.5
if vino >= c:
    vino_r = math.floor(vino)
    print(f'Good harvest this year! Total wine: {vino_r} liters.')
    vino_rest = vino-c
    vino_per1 = (vino_rest/d)
    print('{0} liters left -> {1} liters per person.'.format(math.ceil(vino_rest), math.ceil(vino_per1)))
else:
    vino_ned = c-vino
    print('It will be a tough winter! More {0} liters wine needed.'.format(math.floor(vino_ned)))
