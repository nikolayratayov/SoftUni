lst = list(input())
lst_new = []
for i in range(0, len(lst)):
    lst_new.append(lst.pop())
print(''.join(lst_new))