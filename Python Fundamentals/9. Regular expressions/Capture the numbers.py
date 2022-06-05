import re

x = ''
while True:
    a = input()
    if a == '':
        break
    x += 'x' + a

regex = re.findall(r'\d+', x)
print(' '.join(regex), end=' ')
