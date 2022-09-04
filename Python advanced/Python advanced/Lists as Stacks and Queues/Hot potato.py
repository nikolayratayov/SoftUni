kids = input().split(' ')
toss = int(input())
idx = -1
num = 0
while True:
    if len(kids) == 1:
        break
    idx += 1
    if idx == len(kids):
        idx = 0
    num += 1
    if num == toss:
        num = 0
        print(f'Removed {kids.pop(idx)}')
        idx -= 1
print(f'Last is {kids[0]}')
