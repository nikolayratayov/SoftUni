a = input()
b = input()
a_list = list(a)
b_list = list(b)

for i in range(len(a)):
    if a[i] == b[i]:
        continue
    a_list[i] = b_list[i]
    nov = ''
    nov = nov.join(a_list)
    print(nov)
