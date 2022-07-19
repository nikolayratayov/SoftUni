def merge_array(left, right):
    result = [None] * (len(left) + len(right))
    left_idx = 0
    right_idx = 0
    result_idx = 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    if left_idx == len(left):
        for i in range(right_idx, len(right)):
            result[result_idx] = right[i]
            result_idx += 1
    else:
        for i in range(left_idx, len(left)):
            result[result_idx] = left[i]
            result_idx += 1

    return result


def merge_sort(a):
    if len(a) == 1:
        return a

    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    return merge_array(merge_sort(left), merge_sort(right))


a = [int(x) for x in input().split(' ')]

print(*merge_sort(a), sep=' ')
