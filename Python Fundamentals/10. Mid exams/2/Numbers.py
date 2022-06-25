integers_str = input().split(' ')
integers = [int(x) for x in integers_str]
average = sum(integers) / len(integers)
integers = sorted(integers, reverse=True)
top_5 = []
count = 0
for i in integers:
    count += 1
    if i > average:
        top_5.append(i)
    if count == 5:
        break
top_5_str = [str(x) for x in top_5]
if len(top_5_str) == 0:
    print('No')
else:
    print(' '.join(top_5_str))
