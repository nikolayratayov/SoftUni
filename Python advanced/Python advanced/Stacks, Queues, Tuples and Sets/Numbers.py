first = set(int(x) for x in input().split(' '))
second = set(int(x) for x in input().split(' '))
n = int(input())
for i in range(n):
    command = input().split(' ')
    if command[0] == 'Add' or command[0] == 'Remove':
        for j in range(2, len(command)):
            if command[0] == 'Add':
                if command[1] == 'First':
                    first.add(int(command[j]))
                elif command[1] == 'Second':
                    second.add(int(command[j]))
            elif command[0] == 'Remove':
                if command[1] == 'First':
                    if int(command[j]) in first:
                        first.remove(int(command[j]))
                elif command[1] == 'Second':
                    if int(command[j]) in second:
                        second.remove(int(command[j]))
    else:
        if first.issubset(second):
            print(True)
        elif second.issubset(first):
            print(True)
        else:
            print(False)
print(*sorted(list(first)), sep=', ')
print(*sorted(list(second)), sep=', ')
