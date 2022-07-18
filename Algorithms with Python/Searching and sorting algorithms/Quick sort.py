def quick_sort(start, end, a):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if a[left] > a[pivot] > a[right]:
            a[left], a[right] = a[right], a[left]
        if a[left] <= a[pivot]:
            left += 1
        if a[right] >= a[pivot]:
            right -= 1

    a[pivot], a[right] = a[right], a[pivot]
    quick_sort(start, right - 1, a)
    quick_sort(left, end, a)


a = [int(x) for x in input().split(' ')]

quick_sort(0, len(a) - 1, a)

print(*a, sep=' ')
