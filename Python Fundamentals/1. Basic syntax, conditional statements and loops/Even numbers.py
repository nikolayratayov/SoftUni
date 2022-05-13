import sys

n = int(input())
for i in range(n):
    a = int(input())
    if a % 2 != 0:
        print(f'{a} is odd!')
        sys.exit()
print('All numbers are even.')