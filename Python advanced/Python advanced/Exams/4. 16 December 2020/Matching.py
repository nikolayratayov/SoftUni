males = [int(x) for x in input().split(' ')]
females = [int(x) for x in input().split(' ')]
matches = 0
while True:
    if len(males) == 0 or len(females) == 0:
        break
    if females[0] <= 0:
        females.pop(0)
        continue
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] % 25 == 0:
        females.pop(0)
        try:
            females.pop(1)
        except:
            pass
        continue
    if males[-1] % 25 == 0:
        males.pop()
        try:
            males.pop()
        except:
            pass
        continue
    if females[0] == males[-1]:
        matches += 1
        females.pop(0)
        males.pop()
    else:
        females.pop(0)
        males[-1] -= 2
print(f'Matches: {matches}')
if len(males) == 0:
    print('Males left: none')
else:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
if len(females) == 0:
    print('Females left: none')
else:
    print(f"Females left: {', '.join(str(x) for x in females)}")
