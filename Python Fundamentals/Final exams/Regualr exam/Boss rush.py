import re


n = int(input())
for _ in range(n):
    boss_title = input()
    regex = r'\|([A-Z]{4}[A-Z]*)\|:#([A-Za-z]+\s[A-Za-z]+)#'
    boss_title_lst = re.findall(regex, boss_title)
    if len(boss_title_lst) == 1 and len(boss_title_lst[0]) == 2:
        print(f'{boss_title_lst[0][0]}, The {boss_title_lst[0][1]}')
        print(f'>> Strength: {len(boss_title_lst[0][0])}')
        print(f'>> Armor: {len(boss_title_lst[0][1])}')
    else:
        print('Access denied!')
