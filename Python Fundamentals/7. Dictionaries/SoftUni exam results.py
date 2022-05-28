mydict = {}
languages = {}
while True:
    a = input()
    if a == 'exam finished':
        break
    a = a.split('-')
    if a[1] == 'banned':
        del mydict[a[0]]
    else:
        if a[0] not in mydict:
            mydict[a[0]] = int(a[2])
        elif a[0] in mydict and int(a[2]) > mydict[a[0]]:
            mydict[a[0]] = int(a[2])
        if a[1] not in languages:
            languages[a[1]] = 1
        else:
            languages[a[1]] += 1

print('Results:')
for i, j in mydict.items():
    print(f'{i} | {j}')
print('Submissions:')
for i, j in languages.items():
    print(f'{i} - {j}')
