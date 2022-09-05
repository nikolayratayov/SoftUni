clothes = [int(x) for x in input().split(' ')]
capacity = int(input())
left_cap = capacity
if len(clothes) > 0 and sum(clothes) > 0 and capacity > 0:
    racks = 1
    while True:
        if len(clothes) == 0:
            break
        el = clothes.pop()
        if el > left_cap:
            racks += 1
            left_cap = capacity
            left_cap -= el
        elif el == left_cap:
            if len(clothes) > 0:
                racks += 1
            left_cap = capacity
        else:
            left_cap -= el
else:
    racks = 0
print(racks)
