import re

a = input()
regex = r'[#||]([A-Za-z\s]+)[#||](\d{2}/\d{2}/\d{2})[#||](\d+)[#||]'
food = 0
x = re.findall(regex, a)
for z in x:
    food += int(z[2])
food = food // 2000
print(f'You have food to last you for: {food} days!')
for maikati in x:
    print(f'Item: {maikati[0]}, Best before: {maikati[1]}, Nutrition: {maikati[2]}')
