def move(row, col):
    if row == rows - 1 and col == cols - 1:
        global counter
        counter += 1
    if col + 1 < cols:
        move(row, col + 1)
    if row + 1 < rows:
        move(row + 1, col)


rows = int(input())
cols = int(input())
counter = 0
move(0, 0)
print(counter)