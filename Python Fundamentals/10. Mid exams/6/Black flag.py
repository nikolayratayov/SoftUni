days = int(input())
plunder = int(input())
target = float(input())
gained = 0
for i in range(1, days + 1):
    gained += plunder
    if i % 3 == 0:
        gained += 0.5 * plunder
    if i % 5 == 0:
        gained *= 0.7

if gained >= target:
    print(f'Ahoy! {gained:.2f} plunder gained.')
else:
    left = gained / target * 100
    print(f'Collected only {left:.2f}% of the plunder.')
