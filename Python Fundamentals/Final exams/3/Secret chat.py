message = input()
while True:
    command = input()
    if command == 'Reveal':
        break
    command = command.split(':|:')
    if command[0] == 'InsertSpace':
        idx = int(command[1])
        message = message[:idx] + ' ' + message[idx:]
        print(message)
    elif command[0] == 'Reverse':
        if command[1] in message:
            idx = message.find(command[1])
            substr = command[1]
            substr = substr[::-1]
            message = message[:idx] + message[idx + len(substr):] + substr
            print(message)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        message = message.replace(command[1], command[2])
        print(message)
print(f'You have a new text message: {message}')
