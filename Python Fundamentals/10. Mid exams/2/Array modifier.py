array_str = input().split(' ')
array = [int(i) for i in array_str]
while True:
    command = input()
    if command == 'end':
        break
    command = command.split(' ')
    if command[0] == 'swap':
        index1 = int(command[1])
        index2 = int(command[2])
        ele1 = array[index1]
        ele2 = array[index2]
        array.pop(index1)
        array.insert(index1, ele2)
        array.pop(index2)
        array.insert(index2, ele1)

    elif command[0] == 'multiply':
        index1 = int(command[1])
        index2 = int(command[2])
        ele1 = array[index1]
        ele2 = array[index2]
        result = ele1 * ele2
        array.pop(index1)
        array.insert(index1, result)
    elif command[0] == 'decrease':
        array = [x - 1 for x in array]
array = [str(x) for x in array]
print(', '.join(array))
