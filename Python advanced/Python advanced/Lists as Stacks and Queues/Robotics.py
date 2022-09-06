def print_time(h, m, s):
    value = ''
    if s < 10:
        value_s = '0' + str(s)
    else:
        value_s = str(s)
    if m < 10:
        value_m = '0' + str(m)
    else:
        value_m = str(m)
    if h < 10:
        value_h = '0' + str(h)
    else:
        value_h = str(h)
    value = '[' + value_h + ':' + value_m + ':' + value_s + ']'
    return value


def decrease_times(robots):
    for i in robots:
        if i[2] == i[1]:
            continue
        i[2] -= 1
        if i[2] == -1:
            i[2] = i[1]


lst_rob = [x for x in input().split(';')]
robots = []
for i in lst_rob:
    name, rob_time = i.split('-')
    left_time = int(rob_time)
    robots.append([name, int(rob_time), left_time])

time_lst = input().split(':')
hh = int(time_lst[0])
mm = int(time_lst[1])
ss = int(time_lst[2])
products = []
while True:
    prod = input()
    if prod == 'End':
        break
    products.append(prod)

while True:
    if len(products) == 0:
        break
    ss += 1
    if ss == 60:
        mm += 1
        ss = 0
        if mm == 60:
            hh += 1
            mm = 0
            if hh == 24:
                hh = 0

    decrease_times(robots)
    for i in robots:
        if i[2] == i[1]:
            i[2] -= 1
            curr_time = print_time(hh, mm, ss)
            print(f'{i[0]} - {products.pop(0)} {curr_time}')
            break
    else:
        products.append(products.pop(0))
