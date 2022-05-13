a = int(input())
prime = True
for i in range(2, a):
    if a % i == 0:
        prime = False
        break
print(prime)