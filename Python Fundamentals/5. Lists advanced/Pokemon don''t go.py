a = input().split(' ')
b = []
removed_el = 0
for i in a:
    b.append(int(i))

while True:
    if len(b) == 0:
        break
    ind = int(input())

    if ind < 0:
        temp = b[0]

        removed_el += temp
        b.pop(0)
        b.insert(0, b[-1])

        temp_ind = -1
        for i in b:
            temp_ind += 1
            if i <= temp:
                b[temp_ind] += temp
            else:
                b[temp_ind] -= temp

    elif ind >= len(b):
        temp = b[-1]

        removed_el += temp
        b.pop()
        b.append(b[0])

        temp_ind = -1
        for i in b:
            temp_ind += 1
            if i <= temp:
                b[temp_ind] += temp
            else:
                b[temp_ind] -= temp

    else:
        temp = b[ind]

        removed_el += temp
        b.pop(ind)
        temp_ind = -1
        for i in b:
            temp_ind += 1
            if i <= temp:
                b[temp_ind] += temp
            else:
                b[temp_ind] -= temp

print(removed_el)
