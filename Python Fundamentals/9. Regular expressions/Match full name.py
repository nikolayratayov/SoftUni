import re
a = input()
reg = re.findall('\\b[A-Z][a-z]+ [A-Z][a-z]+\\b', a)
print(' '.join(reg))
