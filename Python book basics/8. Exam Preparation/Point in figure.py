x = int(input())
y = int(input())
vatre = 4 <= x <= 10 and -5 <= y <= 3
vatre_lqvo = 2 <= x <= 4 and -3 <= y <= 1
vatre_dqsno = 10 <= x <= 12 and -3 <= y <= 1
if vatre or vatre_dqsno or vatre_lqvo:
    print('in')
else:
    print('out')
