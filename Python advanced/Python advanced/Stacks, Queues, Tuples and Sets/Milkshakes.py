chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = [int(x) for x in input().split(', ')]
made = 0
while made < 5:
    if len(chocolates) == 0 or len(cups_of_milk) == 0:
        break

    cup = cups_of_milk[0]
    if cup <= 0:
        cups_of_milk.pop(0)
        if cup == chocolates[-1]:
            chocolates.pop()
        continue
    choco = chocolates[-1]
    if choco <= 0:
        chocolates.pop()
        continue
    if choco == cup:
        made += 1
        chocolates.pop()
        cups_of_milk.pop(0)
        continue
    cups_of_milk.append(cups_of_milk.pop(0))
    chocolates[-1] -= 5
if made == 5:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if len(chocolates) > 0:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print('Chocolate: empty')
if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print('Milk: empty')
