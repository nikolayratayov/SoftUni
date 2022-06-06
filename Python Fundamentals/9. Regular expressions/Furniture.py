import re


names_list = []
total_sum = 0
while True:
    a = input()
    if a == 'Purchase':
        break
    valid = re.search(r'>>[a-zA-Z]+<<\d+.?\d+!\d+', a)
    if valid:
        name = re.search(r'>>([a-zA-Z]+)<<', a)
        names_list.append(name.group(1))
        price = re.search(r'<<(\d+.?\d+)!', a)
        quantity = re.search(r'!(\d+)', a)
        total = float(price.group(1)) * int(quantity.group(1))
        total_sum += total

print('Bought furniture:')
for i in names_list:
    print(i)
print(f'Total money spend: {total_sum:.2f}')
