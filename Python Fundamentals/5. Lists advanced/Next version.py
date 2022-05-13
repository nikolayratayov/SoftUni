a = input().split('.')
b = ''
for i in a:
    b += i
b = int(b)
b += 1
b = str(b)
print(f'{b[0]}.{b[1]}.{b[2]}')
