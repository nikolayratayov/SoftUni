bowls = [int(x) for x in input().split(', ')]
customers = [int(x) for x in input().split(', ')]

while True:
    if len(customers) == 0:
        print('Great job! You served all the customers.')
        if len(bowls) > 0:
            print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
        break
    if len(bowls) == 0:
        print('Out of ramen! You didn\'t manage to serve all customers.')
        print(f"Customers left: {', '.join(str(x) for x in customers)}")
        break
    bowl = bowls[-1]
    customer = customers[0]
    if bowl == customer:
        bowls.pop()
        customers.pop(0)
    elif bowl > customer:
        bowls[-1] -= customer
        customers.pop(0)
    else:
        customers[0] -= bowl
        bowls.pop()
