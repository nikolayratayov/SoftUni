lst = []
while True:
    name = input()
    if name == 'End':
        print(f'{len(lst)} people remaining.')
        break
    if name == 'Paid':
        print('\n'.join(lst))
        lst = []
    else:
        lst.append(name)
