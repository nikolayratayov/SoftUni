def move(lab, row, col, path):
    if row < 0 or col < 0 or row == rows or col == cols:
        return

    if lab[row][col] == '*':
        return

    if lab[row][col] == 'e':
        whole_path.append(path)
        print(''.join(whole_path[1::]))
        whole_path.pop()
        return

    if lab[row][col] == 'v':
        return

    lab[row][col] = 'v'
    whole_path.append(path)

    move(lab, row, col - 1, 'L')
    move(lab, row - 1, col, 'U')
    move(lab, row, col + 1, 'R')
    move(lab, row + 1, col, 'D')
    whole_path.pop()
    lab[row][col] = '-'


whole_path = []
rows = int(input())
cols = int(input())
lab = []
for row in range(rows):
    lab.append(list(input()))

move(lab, 0, 0, '')
