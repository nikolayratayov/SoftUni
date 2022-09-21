counter = 0
lines = 0
with open('text.txt') as f:
    for i in f:
        lines += 1
with open('text.txt') as f:
    with open('output.txt', 'w') as out:
        for line in f:
            counter += 1
            letters = 0
            punctuations = 0
            line_to_write = line.replace('\n', '')
            for i in line_to_write:
                if ord(i) in range(65, 91) or ord(i) in range(97, 123):
                    letters += 1
                elif ord(i) in range(33, 35) or ord(i) in range(39, 42) or ord(i) in range(44, 47) or ord(i) in range(
                        58, 60) \
                        or ord(i) == 63 or ord(i) == 91 or ord(i) == 93 or ord(i) == 96 or ord(i) == 123 or \
                        ord(i) == 125:
                    punctuations += 1
            if counter == lines:
                out.write(f'Line {counter}: {line_to_write} ({letters})({punctuations})')
            else:
                out.write(f'Line {counter}: {line_to_write} ({letters})({punctuations})\n')
