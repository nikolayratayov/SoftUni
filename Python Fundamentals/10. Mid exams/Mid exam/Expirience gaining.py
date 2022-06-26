exp_needed = float(input())
battles = int(input())
exp_gain = 0
count = 0
for i in range(1, battles + 1):
    count += 1
    gain = float(input())
    exp_gain += gain
    if i % 3 == 0:
        exp_gain += gain * 0.15
    if i % 5 == 0:
        exp_gain -= gain * 0.1
    if i % 15 == 0:
        exp_gain += gain * 0.05
    if exp_gain >= exp_needed:
        break
if exp_gain >= exp_needed:
    print(f'Player successfully collected his needed experience for {count} battles.')
else:
    print(f'Player was not able to collect the needed experience, {(exp_needed - exp_gain):.2f} more needed.')
