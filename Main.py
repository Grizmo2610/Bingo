from random import randint
import os
import time

COLOR_RED = '\033[91m'
COLOR_CYAN = '\033[96m'


def printBoard(board: list[list[int]]):
    print(COLOR_CYAN + ".____" * 5 + ".")
    for i in range(5):
        print("|    " * 5, end="|\n")
        for j in range(5):
            if board[i][j] != 0:
                print(f"| {board[i][j]:02d}", end=" ")
            else:
                print("|", COLOR_RED +
                      f"{board[i][j]:02d}" + COLOR_CYAN, end=" ")
        print("|\n" + "|____" * 5 + "|")


def pick(number: int, board: list[list[int]]):
    for i in range(5):
        for j in range(5):
            if board[i][j] == number:
                board[i][j] = 0
                break


def countRow(board: list[list[int]]):
    count = 0
    for i in range(5):
        if board[i].count(0) == 5:
            count += 1
    return count


def countColumn(board: list[list[int]]):
    count = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if board[j][i] == 0:
                temp += 1
        if temp == 5:
            count += 1
    return count


def countDiagonal(board: list[list[int]]):
    count = 0
    temp = 0
    for i in range(5):
        if board[i][i] == 0:
            temp += 1

    if temp == 5:
        count += 1

    temp = 0
    for i in range(5):
        if board[i][4 - i] == 0:
            temp += 1

    if temp == 5:
        count += 1

    return count


def randomBoard():
    board = [[0 for i in range(5)] for i in range(5)]
    numbers = [0 for i in range(25)]
    for i in range(1, 26):
        num = randint(0, 24)
        while numbers[num] != 0:
            num = randint(0, 24)
        numbers[num] = i

    for i in range(5):
        for j in range(5):
            board[i][j] = numbers.pop()
    return board


def pickNumber(board):
    while True:
        try:
            number = input("Chọn 1 số trong bảng của bạn: ").capitalize()
            number = int(number)
            if number < 0 or number > 25:
                print("Chỉ chọn số từ 1 đến 25!")
            else:
                break
        except:
            if number == "-26/10/2003":
                printBoard(board)
            elif number == '-r  ule':
                rule()
            else:
                print("Vui lòng chỉ nhập số!")

    return number


def countLine(board):
    return countColumn(board) + countRow(board) + countDiagonal(board)


def play(name: str, board: list[list[int]], other: list[list[int]], sec: int = 5):
    print("Lượt của", name, "! Hiện tại bạn đang có tổng cộng:",
          countLine(board), "đường thẳng\nĐây là bảng của bạn: ")
    printBoard(board)
    number = pickNumber(other)
    while sum([board[i].count(number) for i in range(5)]) == 0:
        print("Số này đã được khoanh rồi! Vui lòng chọn một con số khác")
        number = pickNumber(other)

    pick(number, board)
    pick(number, other)
    if countLine(board) < 5:
        print("Bảng sau khi được tích! Bạn sẽ có", sec, "giây để quan sát")
        printBoard(board)

        # Comment đoạn này nếu như muốn loại bỏ đoạn dừng và xóa màn hình
        time.sleep(sec)
        nextTurn()


def nextTurn(wait: int = 5):
    os.system('cls')
    print("Vui lòng chuyển máy cho người chơi tiếp theo!")
    print("Đếm ngược thời gian chờ chuyển máy!")
    for i in range(wait):
        print(wait - i)
        time.sleep(1)
    os.system('cls')


def victory(name: str):
    os.system('cls')
    print("Chúc mừng", name, "đã dành chiến thắng!")


def ready():
    print()
    temp = input("Nhập Y/N: ").capitalize()
    while temp != "Y" and temp and "N":
        print("Chỉ nhập Y/N: ")
        temp = input("Nhập Y/N: ").capitalize()


def rule():
    print(COLOR_CYAN)
    print("""BINGO!
    Chào mừng tới trò chơi Bingo!
    Bạn sẽ nhận được một bảng 5x5 gồm các số từ 1 đến 25
    Lần lượt mỗi người sẽ chọn 1 số. 
    Sau khi người chọn số tất cả người chơi sẽ khoanh tròn vào con số vừa được gọi sau đó đổi lượt cho người tiếp theo.
    Nhiệm vụ của bạn là khiến tổng số đường thẳng hợp lệ bằng 5 nhanh nhất.
    Đường thẳng hợp lệ được định nghĩa là 5 số thẳng nhau trên 1 hàng thẳng.

    Chú ý: ở trong trò chơi này những ô đã được khoanh sẽ được chuyển thành 00 và tô đỏ""")


rule()
if ready() != 'N':
    namePlayer1 = str(input("Tên người chơi 1: "))
    namePlayer2 = str(input("Tên người chơi 2: "))

    player1 = randomBoard()
    player2 = randomBoard()

    os.system('cls')
    while countLine(player1) < 5 and countLine(player2) < 5:
        play(namePlayer1, player1, player2)

        if countLine(player1) == 5:
            victory(namePlayer1)
            break

        elif countLine(player2) == 5:
            victory(namePlayer2)
            break

        play(namePlayer2, player2, player1)

        if countLine(player1) == 5:
            victory(namePlayer1)
            break

        elif countLine(player2) == 5:
            victory(namePlayer2)
            break

    print()

    print("Bảng của 2 người chơi: ")

    print("Bảng của người chơi", namePlayer1)
    printBoard(player1)

    print()

    print("Bảng người chơi", namePlayer2)
    printBoard(player2)

    print("Cảm ơn bạn đã chơi trò chơi này")

print('Tạm biệt')