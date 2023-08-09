import random

# Hàm in bảng
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Hàm kiểm tra chiến thắng
def check_win(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Hàm kiểm tra hòa
def check_draw(board):
    return all(cell != '-' for row in board for cell in row)

# Hàm tính giá trị của nút lá dựa trên trạng thái của bảng
def evaluate(board):
    if check_win(board, 'X'):
        return 10
    elif check_win(board, 'O'):
        return -10
    return 0

# Hàm Minimax
def minimax(board, depth, is_maximizer):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if check_draw(board):
        return 0

    if is_maximizer:
        best_score = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = '-'
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = '-'
                    best_score = min(best_score, score)
        return best_score

# Hàm tìm nước đi tốt nhất cho máy tính
def find_best_move(board):
    best_move = (-1, -1)
    best_score = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = '-'
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Hàm chơi Tic-Tac-Toe
def play_tic_tac_toe():
    board = [['-' for _ in range(3)] for _ in range(3)]
    print("Trò chơi Tic-Tac-Toe với máy tính (X) và bạn (O)")
    print_board(board)
    
    while True:
        player_row = int(input("Nhập số hàng (0-2): "))
        player_col = int(input("Nhập số cột (0-2): "))
        
        if board[player_row][player_col] == '-':
            board[player_row][player_col] = 'O'
            print_board(board)
            
            if check_win(board, 'O'):
                print("Bạn thắng!")
                break
            elif check_draw(board):
                print("Trận đấu hòa!")
                break
        else:
            print("Vị trí đã được đánh, vui lòng chọn vị trí khác!")    
        
        row, col = find_best_move(board)
        board[row][col] = 'X'
        print("Máy tính đánh tại vị trí ({}, {})".format(row, col))
        print_board(board)

        if check_win(board, 'X'):
            print("Máy tính thắng!")
            break
        elif check_draw(board):
            print("Trận đấu hòa!")
            break


# Bắt đầu trò chơi
play_tic_tac_toe()
