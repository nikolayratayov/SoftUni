def gd(a):
    a *= 2
    print('-' * a)


def sreda(a):
    for k in range(a - 2):
        print('-', end='')
        for i in range(a - 1):
            print('\\/', end='')
        print('-')


a = int(input())

gd(a)
sreda(a)
gd(a)
