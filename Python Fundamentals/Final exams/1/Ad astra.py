import re

a = input()
regex = r'([#\|])([A-Za-z\s]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1'
food = 0
x = re.findall(regex, a)
for z in x:
    food += int(z[3])
food = food // 2000
print(f'You have food to last you for: {food} days!')
for maikati in x:
    if 0 <= int(maikati[3]) <= 10000:
        print(f'Item: {maikati[1]}, Best before: {maikati[2]}, Nutrition: {maikati[3]}')
