a = input()
b = a.split(', ')
b.reverse()
c = 'wolf'
if b[0] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    print(f'Oi! Sheep number {b.index(c)}! You are about to be eaten by a wolf!')
