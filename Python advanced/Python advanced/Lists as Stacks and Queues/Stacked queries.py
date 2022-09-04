n = int(input())
lst = []
for i in range(n):
    command = input()
    if command == '2':
        try:
            lst.pop()
        except:
            pass
    elif command == '3':
        try:
            print(max(lst))
        except:
            pass
    elif command == '4':
        try:
            print(min(lst))
        except:
            pass
    else:
        push, num = command.split(' ')
        lst.append(int(num))
print(*reversed(lst), sep=', ')
