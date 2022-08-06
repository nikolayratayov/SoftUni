password = input()
while True:
    command = input().split(' ')
    if command[0] == 'Done':
        break
    elif command[0] == 'TakeOdd':
        new = password
        password = ''
        for i in range(1, len(new), 2):
            password += new[i]
        print(password)
    elif command[0] == 'Cut':
        idx = int(command[1])
        length = int(command[2])
        password = password[:idx] + password[(idx + length):]
        print(password)
    elif command[0] == 'Substitute':
        if command[1] in password:
            password = password.replace(command[1], command[2])
            print(password)
        else:
            print('Nothing to replace!')
print(f'Your password is: {password}')
