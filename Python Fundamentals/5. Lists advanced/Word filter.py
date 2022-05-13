a = input().split(' ')
b = [x for x in a if len(x) % 2 == 0]
for i in b:
    print(i)