n = int(input())
total = 0
for i in range(n):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if price < 0.01 or price > 100 or days not in range(1, 32) or capsules not in range(1, 2001):
        continue
    cena = price * days * capsules
    total += cena
    print(f'The price for the coffee is: ${cena:.2f}')
print(f'Total: ${total:.2f}')
