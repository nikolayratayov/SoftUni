import re


while True:
    a = input()
    if a == '':
        break
    link = re.search(r'www[.][a-zA-Z0-9-]+([.][a-z]+)+', a)
    if link:
        print(link.group())
