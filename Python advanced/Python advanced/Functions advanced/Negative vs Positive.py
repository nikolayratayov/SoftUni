nums = [int(x) for x in input().split(' ')]
sum_pos = 0
sum_neg = 0
for i in nums:
    if i > 0:
        sum_pos += i
    else:
        sum_neg += i
print(sum_neg)
print(sum_pos)
if sum_pos > abs(sum_neg):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')
