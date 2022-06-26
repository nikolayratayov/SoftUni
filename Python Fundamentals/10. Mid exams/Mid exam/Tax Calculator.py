vehicles = input().split('>>')
agency = 0
for i in vehicles:
    vehicle = i.split(' ')
    type = vehicle[0]
    years = int(vehicle[1])
    kilometers = int(vehicle[2])
    if type == 'family':
        tax = kilometers // 3000 * 12 + (50 - (years * 5))
        print(f'A {type} car will pay {tax:.2f} euros in taxes.')
        agency += tax
    elif type == 'heavyDuty':
        tax = kilometers // 9000 * 14 + (80 - (years * 8))
        print(f'A {type} car will pay {tax:.2f} euros in taxes.')
        agency += tax
    elif type == 'sports':
        tax = kilometers // 2000 * 18 + (100 - (years * 9))
        print(f'A {type} car will pay {tax:.2f} euros in taxes.')
        agency += tax
    else:
        print('Invalid car type.')
print(f'The National Revenue Agency will collect {agency:.2f} euros in taxes.')
