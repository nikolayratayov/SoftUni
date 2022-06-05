import re


a = input()

regex = re.findall(r'[\s^]([0-9a-zA-Z]+[.,\-_]?[0-9a-zA-]+@[a-zA-Z\-]+[.][a-zA-Z-]+[.]?[a-zA-Z]+)', a)
for i in regex:
    print(i)
