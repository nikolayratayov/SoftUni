def chars (a, b):
    str = ''
    for i in range(ord(a) + 1, ord(b)):
        str += ' ' + chr(i)
    return str


a = input()
b = input()

print(chars(a, b))
