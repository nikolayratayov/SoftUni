import re


a = input()
regex = re.findall(r'\b(\d{2})([.\-/])([A-Z][a-z]{2})\2(\d{4})\b', a)
for i in regex:
    print(f'Day: {i[0]}, Month: {i[2]}, Year: {i[3]}')
