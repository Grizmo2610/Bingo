import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 17)

def is_winner(board, player):
    # Kiểm tra hàng ngang
    for row in board:
        if all(symbol == player for symbol in row):
            return True

    # Kiểm tra cột dọc
    for col in range(5):
        if all(row[col] == player for row in board):
            return True

    # Kiểm tra đường chéo chính
    if all(board[i][i] == player for i in range(5)):
        return True

    # Kiểm tra đường chéo phụ
    if all(board[i][4 - i] == player for i in range(5)):
        return True

    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def evaluate(board):
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    if is_winner(board, "X"):
        return 1
    if is_winner(board, "O"):
        return -1
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -float("inf")
        for i in range(5):
            for j in range(5):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(5):
            for j in range(5):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_eval = -float("inf")
    best_move = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[" " for _ in range(5)] for _ in range(5)]

    while not is_board_full(board):
        print_board(board)

        if is_winner(board, "X"):
            print("Bạn thắng!")
            break

        if is_board_full(board):
            print("Hòa!")
            break
        
        while True:
            try:
                user_input = input("Nhập vị trí (theo định dạng x,y): ")
                x, y = map(int, user_input.split(","))
                if board[x][y] == " ":
                    board[x][y] = "O"
                    break
                else:
                    print("Vị trí đã được đánh, vui lòng chọn lại.")
            except (ValueError, IndexError):
                print("Vị trí không hợp lệ, vui lòng chọn lại.")

        x, y = find_best_move(board)
        board[x][y] = "X"

        if is_winner(board, "X"):
            print_board(board)
            print("Máy thắng!")
            break

        if is_board_full(board):
            print("Hòa!")
            break

if __name__ == "__main__":
    main()
