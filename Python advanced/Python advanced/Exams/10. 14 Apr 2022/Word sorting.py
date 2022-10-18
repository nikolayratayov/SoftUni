def words_sorting(*args):
    def sum_digits(word):
        res = 0
        for i in word:
            res += ord(i)
        return res

    words = {}
    sum_values = 0
    for i in args:
        words[i] = sum_digits(i)
        sum_values += sum_digits(i)
    if sum_values % 2 == 0:
        sorted_dict = {k: v for k, v in sorted(words.items(), key=lambda x: x[0])}
    else:
        sorted_dict = {k: v for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True)}
    res = ''
    for k, v in sorted_dict.items():
        res += f'{k} - {v}\n'
    return res[0:len(res) - 1]
