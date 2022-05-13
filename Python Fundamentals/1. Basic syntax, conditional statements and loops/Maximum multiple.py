delitel = int(input())
granica = int(input())
for i in range(granica, 0, -1):
    if i % delitel == 0:
        print(i)
        break
