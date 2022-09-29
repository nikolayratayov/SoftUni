import sys


def check_found_word(words):
    for i in range(len(words)):
        if len(words[i]) == 0:
            if i == 0:
                print(f'Word found: rose')
            elif i == 1:
                print(f'Word found: tulip')
            elif i == 2:
                print(f'Word found: lotus')
            else:
                print(f'Word found: daffodil')
            if len(vowels) > 0:
                print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
            if len(consonants) > 0:
                print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
            sys.exit()


vowels = [x for x in input().split(' ')]
consonants = [x for x in input().split(' ')]
words = ['rose', 'tulip', 'lotus', 'daffodil']
while True:
    if len(vowels) == 0 or len(consonants) == 0:
        break
    first = vowels.pop(0)
    second = consonants.pop()
    for i in range(len(words)):
        for letter in words[i]:
            if first == letter:
                words[i] = words[i].replace(first, '')
                check_found_word(words)
        for letter in words[i]:
            if second == letter:
                words[i] = words[i].replace(second, '')
                check_found_word(words)


print('Cannot find any word!')
if len(vowels) > 0:
    print(f"Vowels left: {' '.join(str(x) for x in vowels)}")
if len(consonants) > 0:
    print(f"Consonants left: {' '.join(str(x) for x in consonants)}")
