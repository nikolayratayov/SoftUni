nums = input().split(' ')
rev_nums = []
for i in range(len(nums)):
    rev_nums.append((nums.pop()))
print(*rev_nums, sep=' ')
