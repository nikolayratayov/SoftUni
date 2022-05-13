a = input().split(' ')
count = len(a) // 2
counter = 0
time1 = 0
time2 = 0
for i in a:
    if counter == count:
        break
    counter += 1
    time1 += int(i)
    if int(i) == 0:
        time1 *= 0.8

revtimes = a[::-1]
counter = 0
for i in revtimes:
    if counter == count:
        break
    counter += 1
    time2 += int(i)
    if int(i) == 0:
        time2 *= 0.8

if time1 < time2:
    print(f'The winner is left with total time: {time1:.1f}')
else:
    print(f'The winner is right with total time: {time2:.1f}')