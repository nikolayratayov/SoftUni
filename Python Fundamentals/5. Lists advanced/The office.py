lst = input().split(' ')
a = int(input())
nov = []
for i in lst:
    nov.append(int(i) * a)
sredno = sum(nov) / len(nov)
happy = 0
for i in nov:
    if i > sredno:
        happy += 1
if happy >= len(nov) / 2:
    print(f'Score: {happy}/{len(nov)}. Employees are happy!')
else:
    print(f'Score: {happy}/{len(nov)}. Employees are not happy!')
