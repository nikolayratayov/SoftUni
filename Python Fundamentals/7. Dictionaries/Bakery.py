a = input().split(' ')
mydict = {}
for i in range(0, len(a), 2):
    mydict[a[i]] = int(a[i + 1])
print(mydict)