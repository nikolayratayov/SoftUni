eee = input().split(' ')
lst = []
for i in eee:
    lst.append(int(i))
while True:
    a = input()
    if a == 'end':
        print(lst)
        break
    a = a.split(' ')

    if a[0] == 'exchange':
        if int(a[1]) < 0 or int(a[1]) >= len(lst):
            print('Invalid index')
        else:
            nach = lst[int(a[1]) + 1:]
            krai = lst[:int(a[1]) + 1]
            lst = nach + krai

    elif a[0] == 'max':
        if a[1] == 'even':
            zap = -1
            index = -1
            sravnenie = -1
            for i in lst:
                index += 1
                if i % 2 == 0 and i >= sravnenie:
                    zap = index
                    sravnenie = i
            if zap < 0:
                print('No matches')
            else:
                print(zap)
        elif a[1] == 'odd':
            zap = -1
            index = -1
            sravnenie = -1
            for i in lst:
                index += 1
                if i % 2 != 0 and i >= sravnenie:
                    zap = index
                    sravnenie = i
            if zap < 0:
                print('No matches')
            else:
                print(zap)

    elif a[0] == 'min':
        if a[1] == 'even':
            zap = -1
            index = -1
            sravnenie = 1001
            for i in lst:
                index += 1
                if i % 2 == 0 and i <= sravnenie:
                    zap = index
                    sravnenie = i
            if zap < 0:
                print('No matches')
            else:
                print(zap)
        elif a[1] == 'odd':
            zap = -1
            index = -1
            sravnenie = 1001
            for i in lst:
                index += 1
                if i % 2 != 0 and i <= sravnenie:
                    zap = index
                    sravnenie = i
            if zap < 0:
                print('No matches')
            else:
                print(zap)

    elif a[0] == 'first':
        samiq_list = []
        if int(a[1]) > len(lst):
            print('Invalid count')
        else:
            if a[2] == 'even':
                for i in lst:
                    if i % 2 == 0 and len(samiq_list) < int(a[1]):
                        samiq_list.append(i)
                print(samiq_list)
            elif a[2] == 'odd':
                for i in lst:
                    if i % 2 != 0 and len(samiq_list) < int(a[1]):
                        samiq_list.append(i)
                print(samiq_list)

    elif a[0] == 'last':
        rev_lst = lst[::-1]
        samiq_list = []
        if int(a[1]) > len(lst):
            print('Invalid count')
        else:
            if a[2] == 'even':
                for i in rev_lst:
                    if i % 2 == 0 and len(samiq_list) < int(a[1]):
                        samiq_list.append(i)
                print(samiq_list[::-1])
            elif a[2] == 'odd':
                for i in rev_lst:
                    if i % 2 != 0 and len(samiq_list) < int(a[1]):
                        samiq_list.append(i)
                print(samiq_list[::-1])
