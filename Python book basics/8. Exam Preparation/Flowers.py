hriz = int(input())
rozi = int(input())
laleta = int(input())
sezon = input().lower()
den = input().lower()
ots1 = 1
ots2 = 1
ots3 = 1
if sezon == 'spring' or sezon == 'summer':
    cenahriz = 2
    cenarozi = 4.1
    cenalale = 2.5
    if den == 'y':
        cenahriz = 2 * 1.15
        cenarozi = 4.1 * 1.15
        cenalale = 2.5 * 1.15
elif sezon == 'autumn' or sezon == 'winter':
    cenahriz = 3.75
    cenarozi = 4.5
    cenalale = 4.15
    if den == 'y':
        cenahriz = 3.75 * 1.15
        cenarozi = 4.5 * 1.15
        cenalale = 4.15 * 1.15
if laleta > 7 and sezon == 'spring':
    ots1 = 0.95
if rozi >= 10 and sezon == 'winter':
    ots2 = 0.9
if rozi + hriz + laleta > 20:
    ots3 = 0.8
krai = (((hriz * cenahriz) + (rozi * cenarozi) + (laleta * cenalale)) * ots1 * ots2 * ots3) + 2
print(f'{krai:.2f}')
