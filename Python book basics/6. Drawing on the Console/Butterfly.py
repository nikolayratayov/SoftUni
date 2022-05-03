n = int(input())
zvz = '*' * (n - 2)
tere = '-' * (n - 2)
inte = ' ' * (n - 1)
for i in range(n - 2):
    if i % 2 == 0:
        print(f'{zvz}' + '\\ /' + f'{zvz}')
    else:
        print(f'{tere}' + '\\ /' + f'{tere}')
print(f'{inte}' + '@')
for x in range(n - 2):
    if x % 2 == 0:
        print(f'{zvz}' + '/ \\' + f'{zvz}')
    else:
        print(f'{tere}' + '/ \\' + f'{tere}')
