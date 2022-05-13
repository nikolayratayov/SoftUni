import sys

red1 = input().split(' ')
red2 = input().split(' ')
red3 = input().split(' ')

if len(set(red1)) == 1:
    if red1[0] == '1':
        print('First player won')
        sys.exit()
    elif red1[0] == '2':
        print('Second player won')
        sys.exit()

if len(set(red2)) == 1:
    if red2[0] == '1':
        print('First player won')
        sys.exit()
    elif red2[0] == '2':
        print('Second player won')
        sys.exit()

if len(set(red3)) == 1:
    if red3[0] == '1':
        print('First player won')
        sys.exit()
    elif red3[0] == '2':
        print('Second player won')
        sys.exit()

if red1[0] == red2[0] == red3[0]:
    if red1[0] == '1':
        print('First player won')
        sys.exit()
    elif red1[0] == '2':
        print('Second player won')
        sys.exit()

if red1[1] == red2[1] == red3[1]:
    if red1[1] == '1':
        print('First player won')
        sys.exit()
    elif red1[1] == '2':
        print('Second player won')
        sys.exit()

if red1[2] == red2[2] == red3[2]:
    if red1[2] == '1':
        print('First player won')
        sys.exit()
    elif red1[2] == '2':
        print('Second player won')
        sys.exit()

if red1[0] == red2[1] == red3[2] or red1[2] == red2[1] == red3[0]:
    if red2[1] == '1':
        print('First player won')
        sys.exit()
    elif red2[1] == '2':
        print('Second player won')
        sys.exit()

print('Draw!')