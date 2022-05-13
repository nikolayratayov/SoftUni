lst = input().split(' ')


def rounds(a):
    nov = []
    for i in a:
        b = round(float(i))
        nov.append(b)
    return nov


print(rounds(lst))