def draw(a):
    print('*' * a)
    if a > 1:
        draw(a - 1)
    print('#' * a)


a = int(input())
draw(a)