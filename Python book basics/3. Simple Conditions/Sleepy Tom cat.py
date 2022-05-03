a = int(input())
b = 30000-((365-a)*63+a*127)
if b >= 0:
    print('Tom sleeps well')
    h = b // 60
    m = b % 60
    print(f'{h} hours and {m} minutes less for play')
else:
    c = abs(b)
    print('Tom will run away')
    h = c // 60
    m = c % 60
    print(f'{h} hours and {m} minutes more for play')
