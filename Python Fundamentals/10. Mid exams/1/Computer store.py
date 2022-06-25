discount = False
price_without_taxes = 0
taxes = 0
while True:
    a = input()
    if a == 'regular':
        break
    elif a == 'special':
        discount = True
        break
    else:
        if float(a) <= 0:
            print('Invalid price!')
            continue
        price_without_taxes += float(a)
        taxes += 0.2 * float(a)
if price_without_taxes == 0:
    print('Invalid order!')
else:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {price_without_taxes:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    if discount:
        total_price = (price_without_taxes + taxes) * 0.9
    else:
        total_price = price_without_taxes + taxes
    print(f'Total price: {total_price:.2f}$')
