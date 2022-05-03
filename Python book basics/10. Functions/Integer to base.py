def int_to_base(number, base):
    result = ''
    while True:
        ost = number % base
        cqlo = number // base
        if cqlo != 0:
            result = str(ost) + result
        else:
            result = str(ost) + result
            return print(result)
        number = cqlo


number = int(input())
base = int(input())
int_to_base(number, base)
