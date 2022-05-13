a = input()
a_list = list(a.split(' '))
nov = []
for i in a_list:
    if int(i) < 0 :
        nov.append(abs(int(i)))
    else:
        nov.append(int(i) - 2 * int(i))

print(nov)
