a = input()
b = int(input())
a_list = list(a.split(', '))
mydict = {}
for i in range(1, b + 1):
    mydict[i] = 0
i = 0
counter = 0
stiga = False
nov = []
while True:
    counter += 1
    i += 1
    if i > len(mydict):
        i = 1

    vremenno = mydict.get(i)
    try:
        mydict[i] = vremenno + int(a_list[counter - 1])
    except:
        mydict[i] = vremenno
        stiga = True

    if stiga:
        break


for i in mydict:
    nov.append(mydict[i])

print(nov)
