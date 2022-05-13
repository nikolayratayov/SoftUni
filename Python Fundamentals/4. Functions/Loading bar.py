def loading(a):
    a = a / 10
    b = 10 - a
    if a == 10:
        print('100% Complete!')
    else:
        print(f'{int(a * 10)}% ', end='')
    print('[', end='')
    print(int(a) * '%' + int(b) * '.', end='')
    print(']')
    if a < 10:
        print('Still loading...')


a = int(input())
loading(a)
