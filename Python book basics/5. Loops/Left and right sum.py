i = int(input())
left_sum = 0
right_sum = 0
for i in range(0, i):
    a = float(input())
    left_sum += a
for i in range(0, i + 1):
    b = float(input())
    right_sum += b
razlika = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {razlika}')
