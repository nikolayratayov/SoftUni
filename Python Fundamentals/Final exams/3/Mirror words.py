import re


text = input()
regex = r'([@|#])([A-Za-z]{2}[A-Za-z]+)\1\1([A-Za-z]{2}[A-Za-z]+)\1'
mathces = re.findall(regex, text)
pairs_lst = []
if len(mathces) > 0:
    valid_pairs = len(mathces)
    for i in mathces:
        one = i[1]
        two = i[2]
        two = two[::-1]
        if one == two:
            pairs_lst.append(i[1] + ' <=> ' + i[2])
    print(f'{valid_pairs} word pairs found!')
    if len(pairs_lst) == 0:
        print('No mirror words!')
    else:
        print(f'The mirror words are:')
        print(', '.join(pairs_lst))
else:
    print('No word pairs found!')
    print('No mirror words!')
