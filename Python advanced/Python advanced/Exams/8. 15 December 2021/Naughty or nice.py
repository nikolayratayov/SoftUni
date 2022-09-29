def naughty_or_nice_list(kids, *args, **kwargs):
    nice = []
    naughty = []
    not_found = []
    nums = [x[0] for x in kids]
    for i in args:
        num, type = [x for x in i.lstrip('(').rstrip(')').split('-')]
        num = int(num)
        if nums.count(num) == 1:
            for idx in range(0, len(kids)):
                if kids[idx][0] == num:
                    if type == 'Nice':
                        nice.append(kids[idx][1])
                    else:
                        naughty.append(kids[idx][1])
                    kids.pop(idx)
                    break
    names = [x[1] for x in kids]
    for k, v in kwargs.items():
        if names.count(k) == 1:
            for idx in range(0, len(kids)):
                if kids[idx][1] == k:
                    if v == 'Nice':
                        nice.append(kids[idx][1])
                    else:
                        naughty.append(kids[idx][1])
                    kids.pop(idx)
                    break
    for i in kids:
        not_found.append(i[1])
    res = ''
    if len(nice) > 0:
        res += f"Nice: {', '.join(nice)}\n"
    if len(naughty) > 0:
        res += f"Naughty: {', '.join(naughty)}\n"
    if len(not_found) > 0:
        res += f"Not found: {', '.join(not_found)}"
    return res
