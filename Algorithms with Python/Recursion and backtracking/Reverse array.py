def reverse_array(arr, left_idx):
    if left_idx == len(arr)// 2:
        return
    right_idx = len(arr) - 1 - left_idx
    arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
    reverse_array(arr, left_idx + 1)


a = [int(x) for x in input().split(' ')]
reverse_array(a, 0)
print(*a, sep=' ')