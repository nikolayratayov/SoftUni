orders = [int(x) for x in input().split(', ')]
employees = [int(x) for x in input().split(', ')]
pizzas = 0
while True:
    if len(orders) == 0:
        print('All orders are successfully completed!')
        print(f'Total pizzas made: {pizzas}')
        print(f"Employees: {', '.join(str(x) for x in employees)}")
        break
    if len(employees) == 0:
        print('Not all orders are completed.')
        print(f"Orders left: {', '.join(str(x) for x in orders)}")
        break
    if orders[0] <= 0 or orders[0] > 10:
        orders.pop(0)
        continue
    if orders[0] <= employees[-1]:
        pizzas += orders[0]
        orders.pop(0)
        employees.pop()
    else:
        pizzas += employees[-1]
        orders[0] -= employees[-1]
        employees.pop()
