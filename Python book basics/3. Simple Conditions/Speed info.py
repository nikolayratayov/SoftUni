a = float(input())
if a <= 10:
    print('slow')
elif 10 < a <= 50:
    print('average')
elif 50 < a <= 150:
    print('fast')
elif 150 < a <= 1000:
    print('ultra fast')
elif a > 1000:
    print('extremely fast')
