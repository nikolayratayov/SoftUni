def vectors(arr, index):
    if index == len(arr):
        print(*arr, sep='')
        return
    for i in range(2):
        arr[index] = i
        vectors(arr, index + 1)


a = int(input())
vector = [0] * a
vectors(vector, 0)
