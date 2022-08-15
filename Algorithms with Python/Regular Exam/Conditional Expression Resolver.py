# t ? t ? t ? 4 : 1 : 2 : 3	     4	    (t ? (t ? (t ? 4 : 1) : 2) : 3)
import re


def find_ans(line):
    line_lst = line.split(' ? ')
    if len(line_lst) == 2:
        numbers_list = line_lst[1].split(' : ')
        if line_lst[0] == 't':
            return numbers_list[0]
        elif line_lst[0] == 'f':
            return numbers_list[1]
    regex = r'([tf]\s\?\s\d+\s:\s\d+)'
    inner = re.search(regex, line).group()
    idx_of_inner = line.find(inner)
    eee = line[:(idx_of_inner - 1)] + ' ' + find_ans(inner) + line[idx_of_inner + len(inner):]
    maikati = len(eee.split(' ? '))
    if maikati > 2:
        find_ans(eee)
    else:
        vai = eee.split(' ? ')
        vai_num = vai[1].split(' : ')
        if vai[0] == 't':
            print(vai_num[0])
        else:
            print(vai_num[1])

line = input()

res = []
offff = line.split(' ? ')
if len(offff) == 2:
    offfff_num = offff[1].split(' : ')
    if offff[0] == 't':
        print(offfff_num[0])
    else:
        print(offfff_num[1])
else:
    find_ans(line)

