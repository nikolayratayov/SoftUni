import re


places = input()
regex = r'([=|/])([A-Z][A-Za-z]{2}[A-Za-z]*)\1'
dest = re.findall(regex, places)
lst_dest = []
sum_points = 0
for i in dest:
    lst_dest.append(i[1])
    sum_points += len(i[1])
print(f"Destinations: {', '.join(lst_dest)}")
print(f'Travel Points: {sum_points}')
