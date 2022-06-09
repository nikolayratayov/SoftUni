import re


total = 0
while True:
    a = input()
    if a == 'end of shift':
        break
    valid = re.search(r'%([A-Z][a-z]+)%.*<([A-Za-z0-9_]+)>.*[|]([0-9]+)[|]\D*([0-9]+[.]?[0-9]+)[$]', a)
    if valid:
        name = valid.group(1)
        product = valid.group(2)
        quantity = int(valid.group(3))
        price = float(valid.group(4))
        total_price = quantity * price
        total += total_price
        print(f'{name}: {product} - {total_price:.2f}')
print(f'Total income: {total:.2f}')
