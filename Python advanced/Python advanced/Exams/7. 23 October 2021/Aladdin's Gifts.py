materials = [int(x) for x in input().split(' ')]
magic_levels = [int(x) for x in input().split(' ')]
gifts = {
    'Gemstone': 0,
    'Porcelain Sculpture': 0,
    'Gold': 0,
    'Diamond Jewellery': 0
}
while True:
    if len(materials) == 0 or len(magic_levels) == 0:
        break
    suma = materials[-1] + magic_levels[0]
    if 100 <= suma <= 199:
        gifts['Gemstone'] += 1
    elif 200 <= suma <= 299:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= suma <= 399:
        gifts['Gold'] += 1
    elif 400 <= suma <= 499:
        gifts['Diamond Jewellery'] += 1
    elif suma < 100:
        if suma % 2 == 0:
            suma = materials[-1] * 2 + magic_levels[0] * 3
        else:
            suma *= 2
        if 100 <= suma <= 199:
            gifts['Gemstone'] += 1
        elif 200 <= suma <= 299:
            gifts['Porcelain Sculpture'] += 1
        elif 300 <= suma <= 399:
            gifts['Gold'] += 1
        elif 400 <= suma <= 499:
            gifts['Diamond Jewellery'] += 1
    elif suma >= 500:
        suma /= 2
        if 100 <= suma <= 199:
            gifts['Gemstone'] += 1
        elif 200 <= suma <= 299:
            gifts['Porcelain Sculpture'] += 1
        elif 300 <= suma <= 399:
            gifts['Gold'] += 1
        elif 400 <= suma <= 499:
            gifts['Diamond Jewellery'] += 1
    materials.pop()
    magic_levels.pop(0)

if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or (gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if len(materials) > 0:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if len(magic_levels) > 0:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
gifts = {k:v for k, v in sorted(gifts.items(), key=lambda x:x[0])}
for k, v in gifts.items():
    if v > 0:
        print(f'{k}: {v}')
