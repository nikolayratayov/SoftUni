elements = input().split(' ')
moves = 0
while True:
    command = input()
    if command == 'end':
        print('Sorry you lose :(')
        print(' '.join(elements))
        break
    command = command.split(' ')
    index1 = int(command[0])
    index2 = int(command[1])
    moves += 1
    if index1 == index2 or index1 < 0 or index1 >= len(elements) or index2 < 0 or index2 >= len(elements):
        add = '-' + str(moves) + 'a'
        index_to_add = int(len(elements) / 2)
        elements.insert(index_to_add, add)
        elements.insert(index_to_add, add)
        print('Invalid input! Adding additional elements to the board')
        continue
    if elements[index1] == elements[index2]:
        element = elements[index1]
        elements.remove(element)
        elements.remove(element)
        print(f'Congrats! You have found matching elements - {element}!')
    else:
        print('Try again!')
    if len(elements) == 0:
        print(f'You have won in {moves} turns!')
        break
