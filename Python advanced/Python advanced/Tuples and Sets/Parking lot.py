n = int(input())
cars = set()
for i in range(n):
    direction, number = [x for x in input().split(', ')]
    if direction == 'IN':
        cars.add(number)
    else:
        cars.remove(number)
if len(cars) == 0:
    print("Parking Lot is Empty")
else:
    print('\n'.join(cars))
