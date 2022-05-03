import math

n = int(input())
if n > 1:
    prime = True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            prime = False
            break
    if prime:
        print('Prime')
    else:
        print('Not prime')
else:
    print('Not prime')
