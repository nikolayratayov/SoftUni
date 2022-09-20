idx = 0
chars_to_replace = {
    '-': '@',
    ',': '@',
    '.': '@',
    '!': '@'
}
with open('text.txt') as f:
    for line in f:
        if idx == 0:
            new_line = line.translate(str.maketrans(chars_to_replace))
            print(' '.join(reversed(new_line[:len(new_line) - 1].split(' '))))
            idx = 1
        elif idx == 1:
            idx = 0
