neighborhood_str = input().split('@')
neighborhood = [int(x) for x in neighborhood_str]
index = 0
while True:
    command = input()
    if command == 'Love!':
        break
    command = command.split(' ')
    index += int(command[1])
    if index >= len(neighborhood):
        index = 0
    if neighborhood[index] == 0:
        print(f'Place {index} already had Valentine\'s day.')
    else:
        neighborhood[index] -= 2
        if neighborhood[index] == 0:
            print(f'Place {index} has Valentine\'s day.')
count = 0
print(f'Cupid\'s last position was {index}.')
if sum(neighborhood) == 0:
    print(f'Mission was successful.')
else:
    for i in neighborhood:
        if i > 0:
            count += 1
    print(f'Cupid has failed {count} places.')
