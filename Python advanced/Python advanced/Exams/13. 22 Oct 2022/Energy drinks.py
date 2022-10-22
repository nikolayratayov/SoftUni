caffeine = [int(x) for x in input().split(', ')]
drinks = [int(x) for x in input().split(', ')]

current_caffeine = 0

while True:
    if len(caffeine) == 0:
        break
    if len(drinks) == 0:
        break
    suma = caffeine[-1] * drinks[0]
    if current_caffeine + suma > 300:
        current_caffeine -= 30
        if current_caffeine < 0:
            current_caffeine = 0
        caffeine.pop()
        drinks.append(drinks.pop(0))
    else:
        current_caffeine += suma
        caffeine.pop()
        drinks.pop(0)
if len(drinks) > 0:
    print(f'Drinks left: {", ".join(str(x) for x in drinks)}')
else:
    print(f'At least Stamat wasn\'t exceeding the maximum caffeine.')
print(f'Stamat is going to sleep with {current_caffeine} mg caffeine.')
