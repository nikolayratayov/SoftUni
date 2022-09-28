energy = [int(x) for x in input().split(' ')]
materials = [int(x) for x in input().split(' ')]
total_energy = 0
toys = 0
count = 0
while True:
    if len(energy) == 0 or len(materials) == 0:
        break
    count += 1
    if energy[0] < 5:
        energy.pop(0)
        continue
    if count % 3 == 0 and count % 5 == 0:
        if energy[0] >= 2 * materials[-1]:
            total_energy += 2 * materials[-1]
            energy[0] -= 2 * materials[-1]
            energy.append(energy.pop(0))
            materials.pop()
        else:
            energy.append(2 * energy.pop(0))
        continue
    if count % 3 == 0:
        if energy[0] >= 2 * materials[-1]:
            total_energy += 2 * materials[-1]
            energy[0] -= 2 * materials[-1]
            energy.append(1 + energy.pop(0))
            toys += 2
            materials.pop()
        else:
            energy.append(2 * energy.pop(0))
        continue
    if count % 5 == 0:
        if energy[0] >= materials[-1]:
            total_energy += materials[-1]
            energy[0] -= materials[-1]
            materials.pop()
            energy.append(energy.pop(0))
        else:
            energy.append(2 * energy.pop(0))
        continue
    if energy[0] >= materials[-1]:
        total_energy += materials[-1]
        energy[0] -= materials[-1]
        energy.append(energy.pop(0) + 1)
        toys += 1
        materials.pop()
    else:
        energy.append(2 * energy.pop(0))

print(f'Toys: {toys}')
print(f'Energy: {total_energy}')
if len(energy) > 0 :
    print(f"Elves left: {', '.join(str(x) for x in energy)}")
if len(materials) > 0:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
