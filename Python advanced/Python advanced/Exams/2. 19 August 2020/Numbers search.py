def numbers_searching(*args):
    nums = sorted(args)
    nums_set = set(nums)
    min_num = min(nums)
    max_num = max(nums)
    list_to_check = [nums.pop(0)]
    duplicates = set()
    for i in range(min_num, max_num + 1):
        if i not in nums_set:
            res = [i]
    for i in range(len(nums)):
        if nums[i] not in list_to_check:
            list_to_check.append(nums[i])
        else:
            duplicates.add(nums[i])
    duplicates = list(duplicates)
    duplicates = sorted(duplicates)
    res.append(duplicates)
    return res
