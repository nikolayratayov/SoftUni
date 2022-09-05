from collections import deque


price = int(input())
size = int(input())
bullets = [int(x) for x in input().split(' ')]
locks = [int(x) for x in input().split(' ')]
value = int(input())
shots = 0
dq = deque(bullets)
counter = 0
while True:
    if len(dq) == 0:
        break

    if counter == size:
        print('Reloading!')
        counter = 0

    if len(locks) == 0:
        break
    el = dq.pop()

    if el <= locks[0]:
        print('Bang!')
        locks.pop(0)
    else:
        print('Ping!')
    counter += 1
    shots += 1

if len(locks) == 0:
    money = value - (shots * price)
    print(f'{len(dq)} bullets left. Earned ${money}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')
