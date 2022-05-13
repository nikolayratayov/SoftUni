budjet = int(input())
while True:
    a = input()
    if a == 'End':
        print('You bought everything needed.')
        break
    a = int(a)
    if a > budjet:
        print('You went in overdraft!')
        break
    budjet -= a
    