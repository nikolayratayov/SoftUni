def check(word):
    for i in word:
        if not i.isalpha() and not i.isdigit() and i != '-' and i != '_':
            return False
    return True


a = input().split(', ')
for i in a:
    if 3 <= len(i) <= 16 and check(i):
        print(i)
