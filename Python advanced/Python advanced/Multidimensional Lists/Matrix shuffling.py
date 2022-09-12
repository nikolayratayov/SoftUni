rows, cols = [int(x) for x in input().split(' ')]
matrix = [[x for x in input().split(' ')] for _ in range(rows)]
while True:
    command = input()
    if command == 'END':
        break
    command = command.split(' ')
    if len(command) != 5 or command[0] != 'swap':
        print('Invalid input!')
        continue
    if int(command[1]) < 0 or int(command[1]) >= rows or int(command[3]) < 0 or int(command[3]) >= rows or int(command[2]) < 0 or int(command[2]) >= cols or int(command[4]) < 0 or int(command[4]) >= cols:
        print('Invalid input!')
        continue
    first = matrix[int(command[1])][int(command[2])]
    second = matrix[int(command[3])][int(command[4])]
    matrix[int(command[1])][int(command[2])] = second
    matrix[int(command[3])][int(command[4])] = first
    for i in matrix:
        print(' '.join(i))
