i = int(input())
even_sum = 0
odd_sum = 0
for i in range(1 , i + 1):
    if i % 2 != 0:
        a = float(input())
        odd_sum += a
    else:
        b = float(input())
        even_sum += b
razlika = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print('Yes')
    print(f'Sum = {even_sum}')
else:
    print('No')
    print(f'Diff = {razlika}')
