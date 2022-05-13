year = int(input())

while True:
    year += 1
    yearlist = list(str(year))
    yearset = set(yearlist)
    if len(yearlist) == len(yearset):
        print(year)
        break

