sequence = input()
lst = []
for i in sequence:
    if i == '(' or i == '[' or i == '{':
        lst.append(i)
    else:
        if len(lst) == 0:
            print('NO')
            break
        if (i == ')' and lst[-1] == '(') or (i == ']' and lst[-1] == '[') or (i == '}' and lst[-1] == '{'):
            lst.pop()
        else:
            print('NO')
            break
else:
    print('YES')
