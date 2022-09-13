def check_knight(board, row, col):
    if row < 0 or col < 0 or row >= n or col >= n:
        return False
    if board[row][col] == 'K':
        return True
    else:
        return False


def check_knight_attacks(board, row, col):
    attacks = 0
    if check_knight(board, row - 2, col + 1):
        attacks += 1
    if check_knight(board, row - 1, col + 2):
        attacks += 1
    if check_knight(board, row + 1, col + 2):
        attacks += 1
    if check_knight(board, row + 2, col + 1):
        attacks += 1
    if check_knight(board, row + 2, col - 1):
        attacks += 1
    if check_knight(board, row + 1, col - 2):
        attacks += 1
    if check_knight(board, row - 1, col - 2):
        attacks += 1
    if check_knight(board, row - 2, col - 1):
        attacks += 1
    return attacks


n = int(input())
board = [list(input()) for _ in range(n)]
removed = 0
while True:
    max_attacks = 0
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                can_attacks = check_knight_attacks(board, row, col)
                if can_attacks > max_attacks:
                    max_attacks = can_attacks
                    max_attack_row_col = [row, col]
    if max_attacks > 0:
        board[max_attack_row_col[0]][max_attack_row_col[1]] = '0'
        removed += 1
    else:
        break
print(removed)
