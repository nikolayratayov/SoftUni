import re


a = input().lower()

x = re.findall('sand', a)
w = re.findall('water', a)
y = re.findall('fish', a)
z = re.findall('sun', a)

print(len(x) + len(w) + len(y) + len(z))
