n = int(input())
word = input()
mylist = []
for i in range(n):
    a = input()
    mylist.append(a)

print(mylist)
newlist = []
for i in mylist:
    if word in i:
        newlist.append(i)

print(newlist)