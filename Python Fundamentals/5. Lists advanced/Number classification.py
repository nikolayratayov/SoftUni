b = input().split(', ')
a = []
for i in b:
    a.append(int(i))
pos = [i for i in a if i >= 0]
neg = [i for i in a if i < 0]
even = [i for i in a if i % 2 == 0]
odd = [i for i in a if i % 2 != 0]
print('Positive:', end=' ')
print(*pos, sep=', ')
print('Negative:', end=' ')
print(', '.join(map(str, neg)))
print('Even:', end=' ')
print(', '.join(map(str, even)))
print('Odd:', end=' ')
print(', '.join(map(str, odd)))