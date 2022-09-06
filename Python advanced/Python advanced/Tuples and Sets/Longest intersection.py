n = int(input())
longest = []
for i in range(n):
    first, second = input().split('-')
    first_start, first_end = [ int(x) for x in first.split(',')]
    second_start, second_end = [ int(x) for x in second.split(',')]
    first_set = set(range(first_start, first_end + 1))
    second_set = set(range(second_start, second_end + 1))
    inter = first_set.intersection(second_set)
    if len(inter) > len(longest):
        longest = sorted(list(inter))

print(f"Longest intersection is [{', '.join(str(x) for x in longest)}] with length {len(longest)}")
