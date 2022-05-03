n = int(input())
stars = 1
if n % 2 == 0:
    stars += 1
left_right = (n - 1) // 2
down = 1
for i in range(0, (n + 1) // 2):
    print('-' * left_right + '*', end='')
    mid = n - 2 * left_right - 2
    if mid >= 0:
        print('-' * mid, end='')
        print('*', end='')
    print('-' * left_right)
    left_right -= 1
for i in range(0, (n - 1) // 2):
    print('-' * down + '*', end='')
    mid = n - 2 * down - 2
    if mid >= 0:
        print('-' * mid, end='')
        print('*', end='')
    print('-' * down)
    down += 1
