def letterize(number):
    minus = number[0]
    if minus == '-' and len(number) == 3:
        return
    if minus == '-' and len(number) == 4:
        print('minus ', end='')
        number = number[1:]
    if len(number) == 3:
        parva = number[0]
        if parva == '0':
            return
        vtora = number[1]
        treta = number[2]
        if parva == '1':
            print('one-hundred', end='')
        elif parva == '2':
            print('two-hundred', end='')
        elif parva == '3':
            print('three-hundred', end='')
        elif parva == '4':
            print('four-hundred', end='')
        elif parva == '5':
            print('five-hundred', end='')
        elif parva == '6':
            print('six-hundred', end='')
        elif parva == '7':
            print('seven-hundred', end='')
        elif parva == '8':
            print('eight-hundred', end='')
        elif parva == '9':
            print('nine-hundred', end='')

        if vtora == '0' and treta == '0':
            print()
            return

        if vtora == '0':
            if treta == '1':
                print(' and one')
            elif treta == '2':
                print(' and two')
            elif treta == '3':
                print(' and three')
            elif treta == '4':
                print(' and four')
            elif treta == '5':
                print(' and five')
            elif treta == '6':
                print(' and six')
            elif treta == '7':
                print(' and seven')
            elif treta == '8':
                print(' and eight')
            elif treta == '9':
                print(' and nine')
            return

        if vtora == '1':
            if treta == '0':
                print(' and ten')
            elif treta == '1':
                print(' and eleven')
            elif treta == '2':
                print(' and twelve')
            elif treta == '3':
                print(' and thirteen')
            elif treta == '4':
                print(' and fourteen')
            elif treta == '5':
                print(' and fifteen')
            elif treta == '6':
                print(' and sixteen')
            elif treta == '7':
                print(' and seventeen')
            elif treta == '8':
                print(' and eighteen')
            elif treta == '9':
                print(' and nineteen')
            return

        if vtora == '2':
            print(' and twenty', end='')
        elif vtora == '3':
            print(' and thirty', end='')
        elif vtora == '4':
            print(' and forty', end='')
        elif vtora == '5':
            print(' and fifty', end='')
        elif vtora == '6':
            print(' and sixty', end='')
        elif vtora == '7':
            print(' and seventy', end='')
        elif vtora == '8':
            print(' and eighty', end='')
        elif vtora == '9':
            print(' and ninety', end='')

        if treta == '0':
            print()
        elif treta == '1':
            print(' one')
        elif treta == '2':
            print(' two')
        elif treta == '3':
            print(' three')
        elif treta == '4':
            print(' four')
        elif treta == '5':
            print(' five')
        elif treta == '6':
            print(' six')
        elif treta == '7':
            print(' seven')
        elif treta == '8':
            print(' eight')
        elif treta == '9':
            print(' nine')


n = int(input())
for i in range(n):
    number = input()
    if int(number) < -999:
        print('too small')
    elif int(number) > 999:
        print('too large')
    else:
        letterize(number)
