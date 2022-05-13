n = int(input())
mylist = []
for i in range(n):
    a = int(input())
    mylist.append(a)

newlist = []

kom = input()

if kom == 'even':
    for i in mylist:
        if i % 2 == 0:
            newlist.append(i)
elif kom == 'odd':
    for i in mylist:
        if i % 2 != 0:
            newlist.append(i)

elif kom == 'negative':
    for i in mylist:
        if i < 0:
            newlist.append(i)

else:
    for i in mylist:
        if i >= 0:
            newlist.append(i)

print(newlist)