a = input().split(', ')
text = input()
for i in a:
    while True:
        if i in text:
            text = text.replace(i, '*' * len(i))
        else:
            break
print(text)
