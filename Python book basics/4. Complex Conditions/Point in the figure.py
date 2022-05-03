h = int(input())
x = int(input())
y = int(input())
out_rectangle1 = (x < 0 or x > 3 * h) or (y < 0 or y > h)
out_rectangle2 = (x < h or x > 2 * h) or (y < 0 or y > 4 * h)
in_rectangle1 = (x > 0 and x < 3 * h) and (y > 0 and y < h)
in_rectangle2 = (x > h and x < 2 * h) and (y > h and y < 4 * h)
common_border = (x > h and x < 2 * h) and y == h
if out_rectangle1 and out_rectangle2:
    print('outside')
elif in_rectangle1 or in_rectangle2 or common_border:
    print('inside')
else:
    print('border')
