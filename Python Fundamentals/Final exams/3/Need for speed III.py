n = int(input())
cars = {}
for _ in range(n):
    car, milleage, fuel = input().split('|')
    cars[car] = [int(milleage), int(fuel)]
while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split(' : ')
    if command[0] == 'Drive':
        if cars[command[1]][1] < int(command[3]):
            print('Not enough fuel to make that ride')
        else:
            fuel_in_car = cars[command[1]][1]
            mill = cars[command[1]][0]
            cars[command[1]] = [mill + int(command[2]), fuel_in_car - int(command[3])]
            print(f'{command[1]} driven for {command[2]} kilometers. {command[3]} liters of fuel consumed.')
        if cars[command[1]][0] >= 100000:
            cars.pop(command[1])
            print(f'Time to sell the {command[1]}!')
    elif command[0] == 'Refuel':
        if int(command[2]) > (75 - cars[command[1]][1]):
            fueled_with = 75 - cars[command[1]][1]
            cars[command[1]][1] = 75
            print(f'{command[1]} refueled with {fueled_with} liters')
        else:
            cars[command[1]][1] += int(command[2])
            print(f'{command[1]} refueled with {command[2]} liters')
    elif command[0] == 'Revert':
        cars[command[1]][0] -= int(command[2])
        print(f'{command[1]} mileage decreased by {command[2]} kilometers')
        if cars[command[1]][0] < 10000:
            cars[command[1]][0] = 10000
for k, v in cars.items():
    print(f'{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.')
