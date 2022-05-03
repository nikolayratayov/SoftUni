end = False
for i in range(1, 4):
    if end == False:
        for j in range(3, 0, -1):
            if i + j == 2:
                end = True
                break
            print(i, j)
