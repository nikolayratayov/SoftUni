import re
a = input()
reg = re.findall(r'\+359\s2\s\d{3}\s\d{4}|\+359-2-\d{3}-\d{4}\b', a)
print(', '.join(reg))
