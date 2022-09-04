import copy

food = int(input())
orders = [int(x) for x in input().split(' ')]
copy_of_orders = copy.copy(orders)
print(max(orders))
for i in orders:
    if i > food:
        print(f"Orders left: {' '.join(str(x) for x in copy_of_orders)}")
        break
    food -= i
    copy_of_orders.pop(0)
else:
    print('Orders complete')
