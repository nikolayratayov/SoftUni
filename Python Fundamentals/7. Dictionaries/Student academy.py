mydict = {}
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    if name not in mydict:
        mydict[name] = list()
        mydict[name].append(grade)
    else:
        mydict[name].append(grade)

for i, j in mydict.items():
    res = sum(j) / len(j)
    if res >= 4.50:
        print(f'{i} -> {res:.2f}')
