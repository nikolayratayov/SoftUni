def check(item, word):
    counter = 0
    for i in word:
        if i == item:
            counter += 1
    return counter


word = input()
mycict = {}
for i in word:
    if i in mycict:
        continue
    mycict[i] = check(i, word)

for k, v in sorted(mycict.items()):
    print(f'{k}: {v} time/s')
