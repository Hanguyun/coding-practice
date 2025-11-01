# 8*8 체스판 위에 8개의 queen이 서로를 죽일 수 없는 자리에 위치히도록 하는 프로그램을 작성하여라.
# 2차원 리스트 사용해야함

N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False

    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    i, j = r - 1, c + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    return True

def place_queens(board, row=0):
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if place_queens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for r in range(N):
        line = []
        for c in range(N):
            line.append('Q' if board[r][c] == 1 else '.')
        print(' '.join(line))
    print()

if not place_queens(board):
    print("해를 찾을 수 없습니다.")
