a = int(input())
if a < 10:
    if a == 0:
        print('zero')
    elif a == 1:
        print('one')
    elif a == 2:
        print('two')
    elif a == 3:
        print('three')
    elif a == 4:
        print('four')
    elif a == 5:
        print('five')
    elif a == 6:
        print('six')
    elif a == 7:
        print('seven')
    elif a == 8:
        print('eight')
    elif a == 9:
        print('nine')
elif 10 <= a < 20:
    b = a // 10
    if b == 1:
        if a == 10:
            print('ten')
        elif a == 11:
            print('eleven')
        elif a == 12:
            print('twelve')
        elif a == 13:
            print('thirteen')
        elif a == 14:
            print('fourteen')
        elif a == 15:
            print('fifteen')
        elif a == 16:
            print('sixteen')
        elif a == 17:
            print('seventeen')
        elif a == 18:
            print('eighteen')
        elif a == 19:
            print('nineteen')
elif 20 <= a < 100:
    b = a // 10
    c = a % 10
    if b == 2:
        text1 = 'twenty'
    elif b == 3:
        text1 = 'thirty'
    elif b == 4:
        text1 = 'forty'
    elif b == 5:
        text1 = 'fifty'
    elif b == 6:
        text1 = 'sixty'
    elif b == 7:
        text1 = 'seventy'
    elif b == 8:
        text1 = 'eighty'
    elif b == 9:
        text1 = 'ninety'
    if c == 1:
        text2 = ' one'
    elif c == 2:
        text2 = ' two'
    elif c == 3:
        text2 = ' three'
    elif c == 4:
        text2 = ' four'
    elif c == 5:
        text2 = ' five'
    elif c == 6:
        text2 = ' six'
    elif c == 7:
        text2 = ' seven'
    elif c == 8:
        text2 = ' eight'
    elif c == 9:
        text2 = ' nine'
    elif c == 0:
        text2 = ''
    print(f'{text1}{text2}')
elif a == 100:
    print('one hundred')
