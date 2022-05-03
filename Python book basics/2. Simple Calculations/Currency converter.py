a = float(input())
ot = input()
kam = input()
if ot == 'USD':
    eee = a * 1.79549
elif ot == 'EUR':
    eee = a * 1.95583
elif ot == 'GBP':
    eee = a * 2.53405
else:
    eee = a
if kam == 'BGN':
    aaa = eee
    print(f'{aaa:.2f} BGN')
elif kam == 'USD':
    aaa = eee / 1.79549
    print(f'{aaa:.2f} USD')
elif kam == 'EUR':
    aaa = eee / 1.95583
    print(f'{aaa:.2f} EUR')
elif kam == 'GBP':
    aaa = eee / 2.53405
    print(f'{aaa:.2f} GBP')
