n = int(input())
m = int(input())
if 2 * n * 2 * n < m:
    print('No')
else:
    for x1 in range(-n, n):
        for y1 in range(-n, n):
            for x2 in range(-n + 1, n + 1):
                for y2 in range(-n + 1, n + 1):
                    if (x2 - x1) * (y2 - y1) >= m and x2 > x1 and y2 > y1:
                        s = (x2 - x1) * (y2 - y1)
                        print(f'({x1}, {y1}) ({x2}, {y2}) -> {s}')
