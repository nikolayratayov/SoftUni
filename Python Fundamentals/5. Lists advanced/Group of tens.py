a = input().split(', ')
lst = []
for i in a:
    lst.append(int(i))
if 10 < max(lst) <= 20:
    b = 2
elif 20 < max(lst) <= 30:
    b = 3
elif 30 < max(lst) <= 40:
    b = 4
elif 40 < max(lst) <= 50:
    b = 5
elif 50 < max(lst) <= 60:
    b = 6
elif 60 < max(lst) <= 70:
    b = 7
elif 70 < max(lst) <= 80:
    b = 8
elif 80 < max(lst) <= 90:
    b = 9
elif 90 < max(lst) <= 100:
    b = 10


tens = [x for x in lst if x <= 10]
tws = [x for x in lst if 10 < x <= 20]
thrs = [x for x in lst if 20 < x <= 30]
fors = [x for x in lst if 30 < x <= 40]
fifs = [x for x in lst if 40 < x <= 50]
sixs = [x for x in lst if 50 < x <= 60]
sevs = [x for x in lst if 60 < x <= 70]
eigs = [x for x in lst if 70 < x <= 80]
nins = [x for x in lst if 80 < x <= 90]
hunds = [x for x in lst if 90 < x <= 100]
vai = [tens, tws, thrs, fors, fifs, sixs, sevs, eigs, nins, hunds]
if max(lst) < 10:
    print(f'Group of 10\'s: {tens}')
else:
    for i in range(b):
        eeeeeee = (i + 1) * 10
        print(f'Group of {eeeeeee}\'s: {vai[i]}')
