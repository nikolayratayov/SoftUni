a = input()
if a == 'int':
    b = int(input())
    print(b * 2)
elif a == 'real':
    b = float(input())
    print(f'{(b * 1.5):.2f}')
elif a == 'string':
    b = input()
    print(f'${b}$')
