guests = {}
disliked_meals = 0
while True:
    command = input().split('-')
    if command[0] == 'Stop':
        break
    elif command[0] == 'Like':
        if command[1] not in guests:
            guests[command[1]] = [command[2]]
        elif command[1] in guests and command[2] not in guests[command[1]]:
            guests[command[1]].append(command[2])
    elif command[0] == 'Dislike':
        if command[1] not in guests:
            print(f'{command[1]} is not at the party.')
        elif command[2] not in guests[command[1]]:
            print(f'{command[1]} doesn\'t have the {command[2]} in his/her collection.')
        else:
            guests[command[1]].remove(command[2])
            disliked_meals += 1
            print(f'{command[1]} doesn\'t like the {command[2]}.')
for k, v in guests.items():
    print(f"{k}: {', '.join(v)}")
print(f'Unliked meals: {disliked_meals}')
