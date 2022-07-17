class Area():
    def __init__(self, row, col, size):
        self.row = row
        self.col = col
        self.size = size


def find_area(board, row, col):
    if row < 0 or row == rows or col < 0 or col == cols:
        return 0
    if board[row][col] != '-':
        return 0

    board[row][col] = '*'
    result = 1
    result += find_area(board, row + 1, col)
    result += find_area(board, row - 1, col)
    result += find_area(board, row, col + 1)
    result += find_area(board, row, col - 1)
    return result


rows = int(input())
cols = int(input())
board = []
for i in range(rows):
    board.append(list(input()))

areas = []
for row in range(rows):
    for col in range(cols):
        size = find_area(board, row, col)
        if size == 0:
            continue
        areas.append(Area(row, col, size))

print(f'Total areas found: {len(areas)}')
for idx, area in enumerate(sorted(areas, key=lambda a: a.size, reverse=True)):
    print(f'Area #{idx + 1} at ({area.row}, {area.col}), size: {area.size}')
