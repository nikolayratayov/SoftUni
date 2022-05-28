contests = {}
while True:
    a = input()
    if a == 'no more time':
        break
    a = a.split(' -> ')
    contest = a[1]
    username = a[0]
    points = int(a[2])
    if contest not in contests:
        contests[contest] = {username: int(points)}
    elif contest in contests and username not in contests[contest]:
        contests[contest][username] = int(points)
    elif contest in contests and username in contests[contest]:
        if points > contests[contest][username]:
            contests[contest][username] = points
users = {}
for i, j in contests.items():
    for user, pointsss in j.items():
        if user not in users:
            users[user] = pointsss
        else:
            users[user] += pointsss

for i in contests:
    count = 0
    print(f'{i}: {len(contests[i])} participants')
    sorted_users_by_name = {k: v for k, v in sorted(contests[i].items(), key=lambda item: item[0])}
    sorted_users_by_points = {k: v for k, v in sorted(sorted_users_by_name.items(), key=lambda item: item[1], reverse=True)}
    for k, v in sorted_users_by_points.items():
        count += 1
        print(f'{count}. {k} <::> {int(v)}')

sorted_users_by_name_total_standings = {k: v for k, v in sorted(users.items(), key=lambda item: item[0])}
sorted_user_by_points_total_standings = {k: v for k, v in sorted(sorted_users_by_name_total_standings.items(), key=lambda item: item[1], reverse=True)}

count = 0
print('Individual standings:')
for k, v in sorted_user_by_points_total_standings.items():
    count += 1
    print(f'{count}. {k} -> {int(v)}')
