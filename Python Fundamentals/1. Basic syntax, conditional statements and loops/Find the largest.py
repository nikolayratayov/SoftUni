a = input()
b = []
for i in a:
    b.append(int(i))
b.sort(reverse=True)
nov = ''
for i in b:
    nov += str(i)

print(nov)
