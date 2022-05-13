a = input()
b = int(input())

a_list = list(a.split(' '))
nov = []
for i in a_list:
    nov.append(int(i))

for i in range(b):
    nov.remove(min(nov))

for i in nov:
    if nov.index(i) == len(nov) - 1:
        print(i)
        break
    print(f'{i}', end=', ')
