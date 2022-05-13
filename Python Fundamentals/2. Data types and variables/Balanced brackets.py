n = int(input())
open = 0
zapen = 0
for i in range(n):
    a = input()
    if a == '(':
        open += 1
    if a == ')':
        zapen += 1
    if open > zapen + 1 or zapen > open + 1:
        open = 999999999

if open == zapen:
    print('BALANCED')
else:
    print('UNBALANCED')