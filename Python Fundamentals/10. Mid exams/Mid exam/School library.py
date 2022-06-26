books = input().split('&')
while True:
    command = input()
    if command == 'Done':
        break
    command = command.split(' | ')
    if command[0] == 'Add Book':
        if command[1] not in books:
            books.insert(0, command[1])
    elif command[0] == 'Take Book':
        if command[1] in books:
            books.remove(command[1])
    elif command[0] == 'Swap Books':
        if command[1] in books and command[2] in books:
            index1 = books.index(command[1])
            index2 = books.index(command[2])
            books.pop(index1)
            books.insert(index1, command[2])
            books.pop(index2)
            books.insert(index2, command[1])
    elif command[0] == 'Insert Book':
        if command[1] not in books:
            books.append(command[1])
    elif command[0] == 'Check Book':
        if int(command[1]) in range(0, len(books)):
            print(books[int(command[1])])
print(', '.join(books))
