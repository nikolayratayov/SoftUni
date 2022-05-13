a = input()
b = int(input())


def calc(a, b):
    if a == 'coffee':
        cena = 1.5
    elif a == 'water':
        cena = 1
    elif a == 'coke':
        cena = 1.4
    elif a == 'snacks':
        cena = 2
    return cena * b


print(f'{(calc(a, b)):.2f}')
