a = input()
go = False
for i in a:
    if go:
        print(f':{i}')
        go =False
    if i == ':':
        go = True
