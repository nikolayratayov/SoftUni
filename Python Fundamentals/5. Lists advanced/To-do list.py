lst = [0] * 10
while True:
    command = input()
    if command == 'End':
        break
    command = command.split('-')
    index = int(command[0]) - 1
    note = command[1]
    lst.pop(index)
    lst.insert(index, note)

res = [x for x in lst if x != 0]
print(res)
