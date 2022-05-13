n = int(input())
free = 0
room = 0
eee = True
for i in range(n):
    room += 1
    a = input().split(' ')
    if len(a[0]) > int(a[1]):
        free += len(a[0]) - int(a[1])
        continue
    elif len(a[0]) < int(a[1]):
        print(f'{int(a[1]) - len(a[0])} more chairs needed in room {room}')
        eee = False
if eee:
    print(f'Game On, {free} free chairs left')
