b = input().split(' ')
a = []
for i in b:
    a.append(int(i))


def eee(a):
    if a % 2 == 0:
        return True
    else:
        return False


maikati = filter(eee, a)
lst = []
for i in maikati:
    lst.append(i)

print(lst)
