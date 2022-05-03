a = input().lower()
summ = 0
for c in a:
    if c == 'a':
        summ += 1
    elif c == 'e':
        summ += 2
    elif c == 'i':
        summ += 3
    elif c == 'o':
        summ += 4
    elif c == 'u':
        summ += 5
print(summ)
