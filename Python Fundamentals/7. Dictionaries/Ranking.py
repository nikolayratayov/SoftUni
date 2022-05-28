contest = {}
while True:
    a = input()
    if a == 'end of contests':
        break
    a = a.split(':')
    contest[a[0]] = a[1]
users = {}
while True:
    a = input()
    if a == 'end of submissions':
        break
    a = a.split('=>')

    if a[0] in contest and a[1] == contest[a[0]]:
        if a[2] not in users:
            users[a[2]] = {a[0]: a[3]}
        elif a[2] in users and a[0] in users[a[2]] and int(a[3]) > int(users[a[2]][a[0]]):
            users[a[2]][a[0]] = a[3]
        elif a[2] in users and a[0] not in users[a[2]]:
            users[a[2]][a[0]] = a[3]
suma = 0
for i, j in users.items():
    temp = 0
    for k, l in j.items():
        temp += int(l)
    if temp > suma:
        best_candidate = i
        suma = temp

print(f'Best candidate is {best_candidate} with total {suma} points.')

users_sort = sorted(users)
print('Ranking:')
for i in users_sort:
    print(i)
    points_sort = sorted(users[i], key=users[i].get, reverse=True)
    for j in points_sort:
        for m, n in users[i].items():
            if m == j:
                print(f'#  {m} -> {n}')
