a = input().split(', ')
hora = []
for i in a:
    hora.append(int(i))
wealth = int(input())
while min(hora) < wealth:
    vzmin = min(hora)
    vzmax = max(hora)
    if vzmax - wealth + vzmin >= wealth:
        vzmax = vzmax - wealth + vzmin
        vzmin = wealth
        hora[hora.index(min(hora))] = vzmin
        hora[hora.index(max(hora))] = vzmax
    else:
        break
if min(hora) < wealth:
    print('No equal distribution possible')
else:
    print(hora)
