def nested_loops(arr, a):
    if a == len(arr):
        print(*arr, sep=' ')
        return
    for i in range(1, n + 1):
        arr[a] = i
        nested_loops(arr, a + 1)


n = int(input())
arr = [None] * n
nested_loops(arr, 0)