def binary_search(a, target):
    left = 0
    right = len(a) - 1
    while True:
        if left > right:
            break
        mid_idx = (left + right) // 2
        mid_el = a[mid_idx]

        if mid_el == target:
            return mid_idx

        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


a = [int(x) for x in input().split(' ')]
target = int(input())

print(binary_search(a, target))
