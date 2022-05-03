a = input().lower()
b = input().lower()
c = float(input())
if a == 'coffee':
    if b == 'sofia':
        print(c*0.5)
    elif b == 'plovdiv':
        print(c*0.4)
    elif b == 'varna':
        print(c*0.45)
elif a == 'water':
    if b == 'sofia':
        print(c*0.8)
    elif b == 'plovdiv':
        print(c*0.7)
    elif b == 'varna':
        print(c*0.7)
elif a == 'beer':
    if b == 'sofia':
        print(round((c*1.2), 2))
    elif b == 'plovdiv':
        print(c*1.15)
    elif b == 'varna':
        print(c*1.1)
elif a == 'sweets':
    if b == 'sofia':
        print(c*1.45)
    elif b == 'plovdiv':
        print(c*1.3)
    elif b == 'varna':
        print(c*1.35)
elif a == 'peanuts':
    if b == 'sofia':
        print(c*1.6)
    elif b == 'plovdiv':
        print(c*1.5)
    elif b == 'varna':
        print(c*1.55)
