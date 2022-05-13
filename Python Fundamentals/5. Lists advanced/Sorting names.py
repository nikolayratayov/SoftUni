lst = input().split(', ')
lst.sort()
lst2 = sorted(lst, key=len, reverse=True)
print(lst2)