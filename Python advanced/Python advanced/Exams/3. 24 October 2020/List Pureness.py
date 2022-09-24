def best_list_pureness(nums, rots):
    best_rots = 0
    best_pureness = 0
    for i in range(0, len(nums)):
        best_pureness += nums[i] * i
    current_rot = 0
    current_pureness = 0
    for _ in range(rots):
        current_rot += 1
        nums.insert(0, nums.pop())
        for i in range(0, len(nums)):
            current_pureness += nums[i] * i
        if current_pureness > best_pureness:
            best_pureness = current_pureness
            best_rots = current_rot
        current_pureness = 0
    return f'Best pureness {best_pureness} after {best_rots} rotations'
