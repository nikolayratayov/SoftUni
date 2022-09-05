import sys


green_light = int(input())
free_window = int(input())
passed = 0
cars = []
passed_cars = []
while True:
    command = input()
    if command == 'END':
        break
    cars.append(command)

for i in cars:
    if i == 'green':
        if len(passed_cars) == 0:
            continue
        counter_enter = green_light
        counter_exit = free_window
        can_enter = True
        passed_this_time = 0
        for j in passed_cars:
            if not can_enter:
                break
            for k in j:
                if counter_enter > 0:
                    counter_enter -= 1
                    if counter_enter == 0:
                        can_enter = False
                else:
                    can_enter = False
                    counter_exit -= 1
                    if counter_exit == -1:
                        print('A crash happened!')
                        print(f'{j} was hit at {k}.')
                        sys.exit()
            passed_this_time += 1
            passed += 1
        for i in range(passed_this_time):
            passed_cars.pop(0)
    else:
        passed_cars.append(i)

print('Everyone is safe.')
print(f'{passed} total cars passed the crossroads.')
