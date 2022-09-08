materials = [int(x) for x in input().split(' ')]
magic_level = [int(x) for x in input().split(' ')]
presents = {}
success = False
while True:
    if len(materials) == 0 or len(magic_level) == 0:
        break
    mat = materials[-1]
    magic = magic_level[0]
    res = mat * magic
    if res == 150:
        if 'Doll' in presents:
            presents['Doll'] += 1
        else:
            presents['Doll'] = 1
        materials.pop()
        magic_level.pop(0)
    elif res == 250:
        if 'Wooden train' in presents:
            presents['Wooden train'] += 1
        else:
            presents['Wooden train'] = 1
        materials.pop()
        magic_level.pop(0)
    elif res == 300:
        if 'Teddy bear' in presents:
            presents['Teddy bear'] += 1
        else:
            presents['Teddy bear'] = 1
        materials.pop()
        magic_level.pop(0)
    elif res == 400:
        if 'Bicycle' in presents:
            presents['Bicycle'] += 1
        else:
            presents['Bicycle'] = 1
        materials.pop()
        magic_level.pop(0)
    else:
        if res < 0:
            sum = mat + magic
            materials.pop()
            magic_level.pop(0)
            materials.append(sum)
        elif res > 0:
            magic_level.pop(0)
            materials[-1] += 15
        else:
            if mat == 0:
                materials.pop()
            if magic == 0:
                magic_level.pop(0)
if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    success = True
if success:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if len(materials) > 0:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if len(magic_level) > 0:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
for k, v in sorted(presents.items()):
    print(f'{k}: {v}')
