import re


attacked = []
destroyed = []
n = int(input())
star = ['s', 'S', 't', 'T', 'a', 'A', 'r', 'R']
for i in range(n):
    count = 0
    a = input()
    for j in a:
        if j in star:
            count += 1
    decrypted = ''
    for j in a:
        decrypted += chr(ord(j) - count)
    regex = re.search(r'.*@([A-Za-z]+)[^-@!:>]*:(\d+).*!([AD])!.*->(\d+).*', decrypted)
    if regex:
        name = regex.group(1)
        type = regex.group(3)
        if type == 'A':
            attacked.append(name)
        else:
            destroyed.append(name)

print(f'Attacked planets: {len(attacked)}')
for i in sorted(attacked):
    print(f'-> {i}')
print(f'Destroyed planets: {len(destroyed)}')
for i in sorted(destroyed):
    print(f'-> {i}')
