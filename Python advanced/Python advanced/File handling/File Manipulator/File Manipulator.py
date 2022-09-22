import os


while True:
    command = input().split('-')
    if command[0] == 'End':
        break
    elif command[0] == 'Create':
        with open(command[1], 'w'):
            pass
    elif command[0] == 'Add':
        with open(command[1], 'a') as f:
            f.write(command[2])
            f.write('\n')
    elif command[0] == 'Replace':
        try:
            with open(command[1]) as f:
                data = f.read()
            data = data.replace(command[2], command[3])
            with open(command[1], 'w') as f:
                f.write(data)
        except FileNotFoundError:
            print('An error occurred')
    elif command[0] == 'Delete':
        try:
            os.remove(command[1])
        except FileNotFoundError:
            print('An error occurred')
