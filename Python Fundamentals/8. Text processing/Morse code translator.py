def translate_letter(a):
    if a == '.-':
        return 'A'
    elif a == '-...':
        return 'B'
    elif a == '-.-.':
        return 'C'
    elif a == '-..':
        return 'D'
    elif a == '.':
        return 'E'
    elif a == '..-.':
        return 'F'
    elif a == '--.':
        return 'G'
    elif a == '....':
        return 'H'
    elif a == '..':
        return 'I'
    elif a == '.---':
        return 'J'
    elif a == '-.-':
        return 'K'
    elif a == '.-..':
        return 'L'
    elif a == '--':
        return 'M'
    elif a == '-.':
        return 'N'
    elif a == '---':
        return 'O'
    elif a == '.--.':
        return 'P'
    elif a == '--.-':
        return 'Q'
    elif a == '.-.':
        return 'R'
    elif a == '...':
        return 'S'
    elif a == '-':
        return 'T'
    elif a == '..-':
        return 'U'
    elif a == '...-':
        return 'V'
    elif a == '.--':
        return 'W'
    elif a == '-..-':
        return 'X'
    elif a == '-.--':
        return 'Y'
    elif a == '--..':
        return 'B'
    else:
        return ''


def translate_word(a):
    new_word = ''
    for i in a:
        new_word += translate_letter(i)
    return new_word


words_lst = input().split(' | ')
translated_words = []
for i in words_lst:
    word = i.split(' ')
    translated_words.append(translate_word(word))

print(' '.join(translated_words))
