karti = input()
broi = int(input())

karti_list = list(karti.split(' '))



def shufle(karti1, karti2, x):
    nov = []
    for i in range(x):
        nov.append(karti1[i])
        nov.append(karti2[i])
    return nov


def split(karti_list):
    kartilist1 = []
    kartilist2 = []
    for i in range(int(len(karti_list) / 2)):
        kartilist1.append(karti_list[i])
        kartilist2.append(karti_list[i + int(len(karti_list) / 2)])
    return kartilist1, kartilist2


x = int(len(karti_list) / 2)

for i in range(broi):
    karti1, karti2 = split(karti_list)
    karti_list = shufle(karti1, karti2, x)

print(karti_list)
