def get_honey(bee, nect, symbol):
    try:
        if symbol == '+':
            res = bee + nect
        elif symbol == '-':
            res = bee - nect
        elif symbol == '*':
            res = bee * nect
        else:
            res = bee / nect
        return abs(res)
    except:
        return 0


bees = [int(x) for x in input().split(' ')]
nectar = [int(x) for x in input().split(' ')]
symbols = input().split(' ')
honey = 0
while True:
    if len(bees) == 0 or len(nectar) == 0:
        break
    bee = bees[0]
    nect = nectar[-1]
    if bee > nect:
        nectar.pop()
        if len(nectar) == 0:
            break
        continue
    honey += get_honey(bees.pop(0), nectar.pop(), symbols.pop(0))
print(f'Total honey made: {honey}')
if len(bees) > 0:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if len(nectar) > 0:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
