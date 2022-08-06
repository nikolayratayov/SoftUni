n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split('<->')
    if plant not in plants:
        plants[plant] = [rarity, []]
    else:
        plants[plant][0] = rarity

while True:
    command = input()
    if command == 'Exhibition':
        break
    command = command.split(': ')
    if command[0] == 'Rate':
        plant, rating = command[1].split(' - ')
        if plant not in plants:
            print('error')
        else:
            plants[plant][1].append(int(rating))
    elif command[0] == 'Update':
        plant, new_rarity = command[1].split(' - ')
        if plant not in plants:
            print('error')
        else:
            plants[plant][0] = new_rarity
    elif command[0] == 'Reset':
        if command[1] not in plants:
            print('error')
        else:
            plants[command[1]][1] = []

print('Plants for the exhibition:')
for k, v in plants.items():
    if len(v[1]) > 0:
        print(f'- {k}; Rarity: {v[0]}; Rating: {(sum(v[1]) / len(v[1])):.2f}')
    else:
        print(f'- {k}; Rarity: {v[0]}; Rating: 0.00')
