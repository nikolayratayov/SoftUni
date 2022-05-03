a = int(input())
b = int(input())
znak = input()
if znak == '+':
    c = a + b
elif znak == '-':
    c = a - b
elif znak == '*':
    c = a * b
elif znak == '/':
    if b == 0:
        a = str(a)
        c = 'Cannot divide ' + a + ' by zero'
        print(c)
    else:
        c = a / b
        c = '{:.2f}'.format(c)
        print(f'{a} / {b} = {c}')
elif znak == '%':
    if b == 0:
        a = str(a)
        c = 'Cannot divide ' + a + ' by zero'
        print(c)
    else:
        c = a % b
        print(f'{a} % {b} = {c}')
if znak == '+' or znak == '-' or znak == '*':
    chetnoiline = c % 2
    if chetnoiline == 0:
        print(f'{a} {znak} {b} = {c} - even')
    else:
        print(f'{a} {znak} {b} = {c} - odd')
