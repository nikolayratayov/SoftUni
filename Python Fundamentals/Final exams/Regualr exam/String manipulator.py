string = input()
while True:
    command = input().split(' ')
    if command[0] == 'End':
        break
    elif command[0] == 'Translate':
        string = string.replace(command[1], command[2])
        print(string)
    elif command[0] == 'Includes':
        print(command[1] in string)
    elif command[0] == 'Start':
        print(string.startswith(command[1]))
    elif command[0] == 'Lowercase':
        string = string.lower()
        print(string)
    elif command[0] == 'FindIndex':
        print(string.rfind(command[1]))
    elif command[0] == 'Remove':
        idx = int(command[1])
        count = int(command[2])
        string = string[:idx] + string[(idx + count):]
        print(string)
