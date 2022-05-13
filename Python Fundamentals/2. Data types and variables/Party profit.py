grupa = int(input())
dni = int(input())
coins = 0
for i in range(1, dni + 1):
    if i % 10 == 0:
        grupa -= 2
    if i % 15 == 0:
        grupa += 5
    coins += 50
    coins -= 2 * grupa
    if i % 3 == 0:
        coins -= 3 * grupa
    if i % 5 == 0:
        coins += 20 * grupa
        if i % 3 == 0:
            coins -= 2 * grupa

coins_na_chovek = coins // grupa

print(f'{grupa} companions received {coins_na_chovek} coins each.')