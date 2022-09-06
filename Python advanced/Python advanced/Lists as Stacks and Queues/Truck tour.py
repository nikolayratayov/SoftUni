def check(idx, circle, res):
    start = idx
    fuel = 0
    while True:
        fuel += circle[idx][0]
        if fuel >= circle[idx][1]:
            fuel -= circle[idx][1]
            idx += 1
            if idx == len(circle):
                idx = 0
            if idx == start:
                res.append(start)
                return
        else:
            return


petrols = int(input())
lst= []
result = []
for i in range(petrols):
    fuel, km = [int(x) for x in input().split(' ')]
    lst.append((fuel, km))

for i in range(petrols):
    check(i, lst, result)
print(min(result))
