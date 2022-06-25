import math


employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students = int(input())
na_chas = employee1 + employee3 + employee2
hours = 0
while True:
    if students <= 0:
        break
    students -= na_chas
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f'Time needed: {hours}h.')
