dispenser = int(input())
people = []
while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    try:
        liters = int(command)
        if dispenser >= liters:
            print(f'{people[0]} got water')
            dispenser -= liters
        else:
            print(f'{people[0]} must wait')
        people.pop(0)
    except:
        if command == 'End':
            break
        refill, liters = command.split(' ')
        liters = int(liters)
        dispenser += liters
print(f'{dispenser} liters left')
