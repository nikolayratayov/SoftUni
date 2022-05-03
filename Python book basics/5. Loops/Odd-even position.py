i = int(input())
summodd = float(0)
maxxodd = float(-1000000000000)
minnodd = float(100000000000)
summeven = float(0)
maxxeven = -float(1000000000000)
minneven = float(100000000000)
for i in range(1, i + 1):
    a = float(input())
    if i % 2 != 0:
        summodd += a
        if a > maxxodd:
            maxxodd = a
        if a < minnodd:
            minnodd = a
    else:
        summeven += a
        if a > maxxeven:
            maxxeven = a
        if a < minneven:
            minneven = a
if i == 1:
    minneven = 'No'
    maxxeven = 'No'
    if summodd % 1 == 0:
        summodd = round(summodd)
    if minnodd % 1 == 0:
        minnodd = round(minnodd)
    if maxxodd % 1 == 0:
        maxxodd = round(maxxodd)
    if summeven % 1 == 0:
        summeven = round(summeven)
    print(f'OddSum={summodd},')
    print(f'OddMin={minnodd},')
    print(f'OddMax={maxxodd},')
    print(f'EvenSum={summeven},')
    print(f'EvenMin={minneven},')
    print(f'EvenMax={maxxeven}')
elif i == 0:
    minnodd = 'No'
    maxxodd = 'No'
    minneven = 'No'
    maxxeven = 'No'
    summodd = round(summodd)
    summeven = round(summeven)
    print(f'OddSum={summodd},')
    print(f'OddMin={minnodd},')
    print(f'OddMax={maxxodd},')
    print(f'EvenSum={summeven},')
    print(f'EvenMin={minneven},')
    print(f'EvenMax={maxxeven}')
else:
    if summodd % 1 == 0:
        summodd = round(summodd)
    if minnodd % 1 == 0:
        minnodd = round(minnodd)
    if maxxodd % 1 == 0:
        maxxodd = round(maxxodd)
    if summeven % 1 == 0:
        summeven = round(summeven)
    if minneven % 1 == 0:
        minneven = round(minneven)
    if maxxeven % 1 == 0:
        maxxeven = round(maxxeven)
    print(f'OddSum={summodd},')
    print(f'OddMin={minnodd},')
    print(f'OddMax={maxxodd},')
    print(f'EvenSum={summeven},')
    print(f'EvenMin={minneven},')
    print(f'EvenMax={maxxeven}')
