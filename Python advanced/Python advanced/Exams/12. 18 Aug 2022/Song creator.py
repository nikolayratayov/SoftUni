def add_songs(*args):
    songs = {}
    for i in args:
        title = i[0]
        text = i[1]
        if title not in songs:
            songs[title] = text
        else:
            for line in text:
                songs[title].append(line)
    res = ''
    for k, v in songs.items():
        res += f'- {k}\n'
        for line in v:
            res += f'{line}\n'
    return res[0:len(res) - 1]
