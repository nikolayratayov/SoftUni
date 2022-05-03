import math
a = input().lower()
praz = int(input())
patuvaniq = int(input())
weeksof = 48-patuvaniq
weekroden = patuvaniq
igrasofia = (3/4*weeksof)+(2/3*praz)
igraroden = patuvaniq
obshto = igraroden + igrasofia
if a == 'leap':
    obshto = math.floor(obshto*0.15+obshto)
    print(obshto)
elif a == 'normal':
    print(math.floor(obshto))
