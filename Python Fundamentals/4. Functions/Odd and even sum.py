def eee(a):
    odd = 0
    even = 0
    for i in a:
        if int(i) % 2 == 0:
            even += int(i)
        else:
            odd += int(i)
    res = f'Odd sum = {odd}, Even sum = {even}'
    return res


a = input()

print(eee(a))
