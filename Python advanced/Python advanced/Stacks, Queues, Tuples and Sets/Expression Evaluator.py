expression = input().split(' ')
res = []

for i in expression:
    if i == '+':
        temp = 0
        for j in res:
            temp += j
        res = [temp]
    elif i == '-':
        temp = res[0]
        for j in range(1, len(res)):
            temp -= res[j]
        res = [temp]
    elif i == '*':
        temp = 1
        for j in res:
            temp *= j
        res = [temp]
    elif i == '/':
        temp = res[0]
        for j in range(1, len(res)):
            temp //= res[j]
        res = [temp]
    else:
        res.append(int(i))
print(res[0])
