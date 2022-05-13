def nehstosi(a, b):
    factA = 1
    factB = 1
    for i in range(1, a + 1):
        factA *= i
    for i in range(1, b + 1):
        factB *= i
    res = factA / factB
    return res


a = int(input())
b = int(input())
print(f'{(nehstosi(a, b)):.2f}')
