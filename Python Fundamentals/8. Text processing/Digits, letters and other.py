a = input()
digits = ''
letters = ''
other = ''
for i in a:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        other += i
print(digits)
print(letters)
print(other)