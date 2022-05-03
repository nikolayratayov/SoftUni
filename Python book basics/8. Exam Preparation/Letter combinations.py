nach = input()
krai = input()
bez = input()
broi = 0
for i in range(ord(nach), ord(krai) + 1):
    for j in range(ord(nach), ord(krai) + 1):
        for k in range(ord(nach), ord(krai) + 1):
            if i == ord(bez) or j == ord(bez) or k == ord(bez):
                continue
            else:
                print(f'{chr(i)}{chr(j)}{chr(k)}', end=' ')
                broi += 1
print(broi)
