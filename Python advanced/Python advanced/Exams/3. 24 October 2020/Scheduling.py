jobs = [int(x) for x in input().split(', ')]
idx = int(input())
cycles = 0
while True:
    current_idx = jobs.index(min(jobs))
    cycles += jobs[current_idx]
    jobs[current_idx] = float('inf')
    if current_idx == idx:
        break
print(cycles)
