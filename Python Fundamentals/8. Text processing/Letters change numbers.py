a = input()
totalsum = 0
digits = ''
occur = 0
for i in a:
    if i == ' ':
        digits = ''
        continue
    else:
        if i.isalpha() and occur == 0:
            first = i
            occur += 1
            continue
        elif i.isdigit():
            digits += i
        elif i.isalpha() and occur == 1:
            occur = 0
            last = i
            number = int(digits)
            if first.isupper():
                first = ord(first) - 64
                number /= first
            else:
                first = ord(first) - 96
                number *= first
            if last.isupper():
                last = ord(last) - 64
                number -= last
            else:
                last = ord(last) - 96
                number += last
            totalsum += number
            continue

print(f'{totalsum:.2f}')