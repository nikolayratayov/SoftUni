def arr_sum(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    return arr[index] + arr_sum(arr, index + 1)


a = [int(x) for x in input().split(' ')]
print(arr_sum(a, 0))