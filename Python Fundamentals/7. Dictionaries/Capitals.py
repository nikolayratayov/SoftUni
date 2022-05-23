keys = input().split(', ')
values = input().split(', ')
mydict = {k: v for (k, v) in zip(keys, values)}
for i in mydict:
    print(f'{i} -> {mydict.get(i)}')
    