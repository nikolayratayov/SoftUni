import re


a = input()
regex = re.finditer(r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))', a)
for i in regex:
    print(i.group(), end=' ')
