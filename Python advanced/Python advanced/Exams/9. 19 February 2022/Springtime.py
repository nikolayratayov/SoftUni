def start_spring(**kwargs):
    new_dict = {}
    for k, v in kwargs.items():
        if v not in new_dict:
            new_dict[v] = []
    for k, v in kwargs.items():
        new_dict[v].append(k)
    new_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda x: x[0])}
    new_dict = {k: v for k, v in sorted(new_dict.items(), key=lambda x: len(x[1]), reverse=True)}
    res = ''
    for k, v in new_dict.items():
        res += f'{k}:\n'
        for i in sorted(v):
            res += f'-{i}\n'
    return res
