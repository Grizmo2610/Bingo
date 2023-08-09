from random import randint

# Định nghĩa các giá trị biểu diễn cho ô trống, người chơi X và người chơi O
EMPTY = '-'
PLAYER_X = 'X'
PLAYER_O = 'O'

def checkWin(board, player):
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Hàm tính giá trị của nút lá dựa trên trạng thái của bảng
def evaluate(board):
    if checkWin(board, PLAYER_O):
        return 10
    elif checkWin(board, PLAYER_X):
        return -10
    return 0

def is_full(board):
    # Kiểm tra xem bàn cờ đã đầy chưa
    for row in board:
        if any(cell == EMPTY for cell in row):
            return False
    return True

# Hàm Minimax
def minimax(board, depth, player):
    score = evaluate(board)
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_full(board):
        return 0
    
    best_score = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = player
                score = minimax(board, depth + 1, player)
                board[i][j] = EMPTY
                best_score = max(best_score, score)
    return best_score
    

# Hàm tìm nước đi tốt nhất cho máy tính
def bestMove(board, player):
    best_move = (-1, -1)
    best_score = float('-inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, player)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def print_board(board):
    for row in board:
        print(' '.join(row))

def main(size: int = 3):
    # Khởi tạo bàn cờ nxn
    board = [[EMPTY for _ in range(size)] for _ in range(size)]
    count = 0
    while not is_full(board) and evaluate(board) == 0:
        # Lượt chơi của người chơi O
        print_board(board)
        while True:
            row, col = map(int, input("Nhập nước đi (hàng và cột, cách nhau bởi dấu cách): ").split())
            if 0 <= row < size and 0 <= col < size and board[row][col] == EMPTY:
                board[row][col] = PLAYER_X
                break
            else:
                print("Ô này không hợp lệ hoặc đã được đánh, vui lòng chọn ô khác!")

        if is_full(board) or evaluate(board) != 0:
            break

        # Lượt chơi của máy tính (người chơi O)
        print("Lượt chơi của máy tính:")
        move = tuple()
        move = bestMove(board, PLAYER_O)
        board[move[0]][move[1]] = PLAYER_O

    # In bàn cờ kết quả sau khi trò chơi kết thúc
    print_board(board)
    result = evaluate(board)
    if result == 10:
        print("Người chơi X thắng!")
    elif result == -10:
        print("Người chơi O thắng!")
    else:
        print("Trò chơi hòa!")

if __name__ == "__main__":
    main(size=3)