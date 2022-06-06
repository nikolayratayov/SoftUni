import re


a = input()
regex = re.findall(r'\b_([0-9a-zA-Z]+)\b', a)
print(','.join(regex))
