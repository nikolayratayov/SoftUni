a = input().split(', ')



def palindrom(a):
    for i in a:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


palindrom(a)

