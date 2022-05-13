import sys

while True:
    a = input()
    if a == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    if a == 'Voldemort':
        print('You must not speak of that name!')
        sys.exit()
    if len(a) < 5:
        print(f'{a} goes to Gryffindor.')
    elif len(a) == 5:
        print(f'{a} goes to Slytherin.')
    elif len(a) == 6:
        print(f'{a} goes to Ravenclaw.')
    else:
        print(f'{a} goes to Hufflepuff.')
