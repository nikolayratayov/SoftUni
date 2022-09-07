n = int(input())
mydict = {}
for i in range(n):
    name, grade = [x for x in input().split(' ')]
    grade = "{:.2f}".format(float(grade))
    if name not in mydict:
        mydict[name] = [grade]
    else:
        mydict[name].append(grade)

for k, v in mydict.items():
    eee = 0
    for i in v:
        eee += float(i)
    average = eee / len(v)
    print(f"{k} -> {' '.join(str(x) for x in v)} (avg: {average:.2f})")
