a = input().split(', ')
while True:
    b = input()
    if b == 'course start':
        break
    b = b.split(':')
    if b[0] == 'Add':
        if b[1] not in a:
            a.append(b[1])
    elif b[0] == 'Insert':
        if b[1] not in a:
            a.insert(int(b[2]), b[1])
    elif b[0] == 'Remove':
        if b[1] in a:
            a.remove(b[1])
            temp = b[1] + '-Exercise'
            if temp in a:
                a.remove(temp)
    elif b[0] == 'Swap':
        if b[1] in a and b[2] in a:
            index1 = a.index(b[1])
            index2 = a.index(b[2])
            if index1 < index2:
                a.remove(b[1])
                a.remove(b[2])
                a.insert(index1, b[2])
                a.insert(index2, b[1])
            else:
                a.remove(b[1])
                a.remove(b[2])
                a.insert(index2, b[1])
                a.insert(index1, b[2])
            temp1 = b[1] + '-Exercise'
            temp2 = b[2] + '-Exercise'
            if temp1 in a:
                a.remove(temp1)
                a.insert(index2 + 1, temp1)
            if temp2 in a:
                a.remove(temp2)
                a.insert(index1 + 1, temp2)
    elif b[0] == 'Exercise':
        temp = b[1] + '-Exercise'
        if b[1] in a and temp not in a:
            index = a.index(b[1])
            a.insert(index + 1, temp)
        elif b[1] in a and temp in a:
            pass
        else:
            a.append(b[1])
            a.append(temp)
count = 0
for i in a:
    count += 1
    print(f'{count}.{i}')
