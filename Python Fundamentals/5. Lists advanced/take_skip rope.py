a = input()
numbers = [int(i) for i in a if i.isdigit()]
maikati = [i for i in a if not i.isdigit()]

nonnumbers = ''
for i in maikati:
    nonnumbers += i

# take = []
# skip = []
# index = -1
# for i in numbers:
#     index += 1
#     if index % 2 == 0:
#         take.append(i)
#     else:
#         skip.append(i)
index = -1
taken = ''
for i in numbers:
    index += 1
    if index % 2 == 0:
        taken += nonnumbers[:i]
        nonnumbers = nonnumbers[i:]
    else:
        nonnumbers = nonnumbers[i:]
print(taken)