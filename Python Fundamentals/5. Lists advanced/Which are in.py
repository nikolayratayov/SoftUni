a = input().split(', ')
b = input().split(', ')
nov = []
for i in a:
    for j in b:
        if i in j:
            nov.append(i)
nov = list(dict.fromkeys((nov)))
print(nov)