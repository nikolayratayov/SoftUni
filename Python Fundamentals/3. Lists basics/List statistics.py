n = int(input())
positive = []
negative = []
for i in range(n):
    a = int(input())
    if a < 0:
        negative.append(a)
    else:
        positive.append(a)
print(positive)
print(negative)
print(f'Count of positives: {len(positive)}')
print(f'Sum of negatives: {sum(negative)}')
