import re


n = int(input())
for i in range(n):
    a = input()
    name = re.search('@.*\|', a).group()
    name = name.replace('@', '')
    name = name.replace('|', '')
    age = re.search('#.*\*', a).group()
    age = age.replace('#', '')
    age = age.replace('*', '')
    print(f'{name} is {age} years old.')
