stops = input()
while True:
    command = input()
    if command == 'Travel':
        break
    command = command.split(':')
    if command[0] == 'Add Stop':
        if 0 <= int(command[1]) < len(stops):
            stops = stops[:int(command[1])] + command[2] + stops[int(command[1]):]
        print(stops)
    elif command[0] == 'Remove Stop':
        start = int(command[1])
        end = int(command[2])
        if 0 <= start < len(stops) and 0 <= end < len(stops):
            stops = stops[:start] + stops[end + 1:]
        print(stops)
    elif command[0] == 'Switch':
        old = command[1]
        new = command[2]
        if old in stops:
            stops = stops.replace(old, new)
        print(stops)
print(f'Ready for world tour! Planned stops: {stops}')
