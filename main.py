gameBoard = {
    "7": " ",
    "8": " ",
    "9": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "1": " ",
    "2": " ",
    "3": " ",
}


def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])


def game():

    turn = "X"
    count = 0

    for i in range(10):
        printBoard(gameBoard)
        print("It's your turn," + turn + ".Move to which place?")
        print("Use numpad notation to choose where you wish to place your mark.")

        move = input()

        if gameBoard[move] == " ":
            gameBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if (
                gameBoard["7"] == gameBoard["8"] == gameBoard["9"] != " "
            ):  # across the top
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif (
                gameBoard["4"] == gameBoard["5"] == gameBoard["6"] != " "
            ):  # across the middle
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif (
                gameBoard["1"] == gameBoard["2"] == gameBoard["3"] != " "
            ):  # across the bottom
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif (
                gameBoard["1"] == gameBoard["4"] == gameBoard["7"] != " "
            ):  # down the left side
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif (
                gameBoard["2"] == gameBoard["5"] == gameBoard["8"] != " "
            ):  # down the middle
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif (
                gameBoard["3"] == gameBoard["6"] == gameBoard["9"] != " "
            ):  # down the right side
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif gameBoard["7"] == gameBoard["5"] == gameBoard["3"] != " ":  # diagonal
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break
            elif gameBoard["1"] == gameBoard["5"] == gameBoard["9"] != " ":  # diagonal
                printBoard(gameBoard)
                print("\nGame Over,\n")
                print(turn + " won.")
                break

        # If neither X nor O wins and the board is full, the game ties.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # This is to change player input after every move.
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    board_keys = []

    for key in gameBoard:
        board_keys.append(key)

        restart = input("Do want to play Again?(y/n)")

    if restart == "y" or restart == "Y":
        for key in board_keys:
            gameBoard[key] = " "


game()
