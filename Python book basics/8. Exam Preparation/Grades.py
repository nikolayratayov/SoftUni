stud = int(input())
slab = 0
sreden = 0
dobar = 0
mn_dobar = 0
average = 0
for i in range(stud):
    ocenka = float(input())
    average += ocenka
    if 2 <= ocenka <= 2.99:
        slab += 1
    elif 3 <= ocenka <= 3.99:
        sreden += 1
    elif 4 <= ocenka <= 4.99:
        dobar += 1
    elif ocenka >= 5:
        mn_dobar += 1
slabperc = slab / stud * 100
sredenperc = sreden / stud * 100
dobarperc = dobar / stud * 100
mn_dobarperc = mn_dobar / stud * 100
sredenuspeh = average / stud
print(f'Top students: {mn_dobarperc:.2f}%')
print(f'Between 4.00 and 4.99: {dobarperc:.2f}%')
print(f'Between 3.00 and 3.99: {sredenperc:.2f}%')
print(f'Fail: {slabperc:.2f}%')
print(f'Average: {sredenuspeh:.2f}')
