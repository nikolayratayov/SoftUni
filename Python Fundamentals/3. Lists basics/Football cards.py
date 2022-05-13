a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


cards = input()
cards_list = list(cards.split(' '))
try:
    for i in cards_list:
        if i[0] == 'A':
            try:
                a.remove(int(i[2:]))
            except:
                pass
        elif i[0] == 'B':
            try:
                b.remove(int(i[2:]))
            except:
                pass
        if len(a) < 7 or len(b) < 7:
            break
except:
    pass
print(f'Team A - {len(a)}; Team B - {len(b)}')

if len(a) < 7 or len(b) < 7:
    print('Game was terminated')
