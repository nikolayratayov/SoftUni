a = int(input())
print(a*'*')
for x in range(a):
    if x == a-2:
        break
    b = (a-2)*' '
    c = '*'
    print(f'{c}{b}{c}')
print(a*'*')