coffee = 0
while True:
    a = input()
    if a == 'END':
        break
    if a == 'coding' or a == 'CODING' or a == 'dog' or a == 'DOG' or a == 'cat' or a == 'CAT' or a == 'movie' or a == 'MOVIE':
        if a.isupper():
            coffee += 2
        else:
            coffee += 1

if coffee > 5:
    print('You need extra sleep')
else:
    print(coffee)
    