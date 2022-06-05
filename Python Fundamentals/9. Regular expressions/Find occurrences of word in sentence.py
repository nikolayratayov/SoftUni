import re


a = input()
b = input()
regex = re.findall(r'\b' + b + r'\b', a, re.IGNORECASE)
print(len(regex))
