n = int(input())
regular = set()
vip = set()
for i in range(n):
    item = input()
    if item[0].isdigit():
        vip.add(item)
    else:
        regular.add(item)

while True:
    item = input()
    if item == 'END':
        break
    if item[0].isdigit():
        vip.remove(item)
    else:
        regular.remove(item)
print(len(regular) + len(vip))
if len(regular) + len(vip) > 0:
    if len(vip) > 0:
        print('\n'.join(sorted(list(vip))))
    if len(regular) > 0:
        print('\n'.join(sorted(list(regular))))
