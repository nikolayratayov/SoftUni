a = input()
while True:
    command = input()
    if command == 'Decode':
        break
    command = command.split('|')
    if command[0] == 'Move':
        n = int(command[1])
        a = a[n:] + a[:n]
    elif command[0] == 'Insert':
        idx = int(command[1])
        value = command[2]
        a = a[:idx] + value + a[idx:]
    elif command[0] == 'ChangeAll':
        sub = command[1]
        repl = command[2]
        a = a.replace(sub, repl)
print(f'The decrypted message is: {a}')
