lists = input().split('|')
lst = []
for i in reversed(lists):
    inner_lst = i.split(' ')
    for j in inner_lst:
        try:
            num = float(j)
            if num % 10 == 0 and num != 0:
                lst.append(num)
            else:
                lst.append(int(j))
        except:
            pass
print(*lst, sep=' ')
