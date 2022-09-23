customers = [int(x) for x in input().split(', ')]
taxis = [int(x) for x in input().split(', ')]
time = 0
while True:
    if len(customers) == 0:
        print('All customers were driven to their destinations')
        print(f'Total time: {time} minutes')
        break
    elif len(taxis) == 0:
        print('Not all customers were driven to their destinations')
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
        break
    if customers[0] <= taxis[-1]:
        time += customers[0]
        customers.pop(0)
        taxis.pop()
    else:
        taxis.pop()
