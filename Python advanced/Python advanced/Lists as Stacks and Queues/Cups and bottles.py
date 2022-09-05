cups = [int(x) for x in input().split(' ')]
bottles = [int(x) for x in input().split(' ')]
wasted = 0
take_cup = True
while True:
    if len(cups) == 0 or len(bottles) == 0:
        break
    bottle = bottles.pop()
    if take_cup:
        cup = cups[0]
    if bottle >= cup:
        cups.pop(0)
        wasted += (bottle - cup)
        take_cup = True
    else:
        cup -= bottle
        take_cup = False

if len(cups) == 0:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles))}")
else:
    print(f"Cups: {' '.join(str(x) for x in cups)}")
print(f'Wasted litters of water: {wasted}')
