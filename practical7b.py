# Tic-Tac-Toe using Minimax Algorithm

import math


# -------------------------------
# 1. Display the board
# -------------------------------
def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


# -------------------------------
# 2. Check winner
# -------------------------------
def check_winner(board):

    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:

        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


# -------------------------------
# 3. Minimax Algorithm
# -------------------------------
def minimax(board, maximizing):

    result = check_winner(board)

    # Computer wins
    if result == "O":
        return 10

    # Human wins
    if result == "X":
        return -10

    # Draw
    if result == "Draw":
        return 0

    # MAX - Computer
    if maximizing:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                # Try O
                board[i] = "O"

                score = minimax(board, False)

                # Undo move
                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    # MIN - Human
    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                # Try X
                board[i] = "X"

                score = minimax(board, True)

                # Undo move
                board[i] = " "

                best_score = min(best_score, score)

        return best_score


# -------------------------------
# 4. Find best move for computer
# -------------------------------
def best_move(board):

    best_score = -math.inf
    best_position = -1

    for i in range(9):

        if board[i] == " ":

            # Try computer move
            board[i] = "O"

            score = minimax(board, False)

            # Undo move
            board[i] = " "

            if score > best_score:
                best_score = score
                best_position = i

    return best_position


# -------------------------------
# 5. Main Program
# -------------------------------

board = [" "] * 9

print("TIC-TAC-TOE")
print("You are X")
print("Computer is O")
print("Positions are 1 to 9")

while True:

    # Display board
    print_board(board)

    # ---------------------------
    # Human move
    # ---------------------------

    try:
        position = int(input("Enter your position (1-9): "))

    except ValueError:
        print("Please enter a number.")
        continue

    # Convert 1-9 to 0-8
    position = position - 1

    # Check valid position
    if position < 0 or position > 8:
        print("Please enter a number between 1 and 9.")
        continue

    # Check occupied position
    if board[position] != " ":
        print("Position already occupied.")
        continue

    # Place X
    board[position] = "X"

    # Check result after human move
    result = check_winner(board)

    if result is not None:

        print_board(board)

        if result == "X":
            print("You win!")

        elif result == "Draw":
            print("Game Draw!")

        break


    # ---------------------------
    # Computer move
    # ---------------------------

    computer_position = best_move(board)

    # Place O
    board[computer_position] = "O"

    print("Computer selected position:",
          computer_position + 1)

    # Check result after computer move
    result = check_winner(board)

    if result is not None:

        print_board(board)

        if result == "O":
            print("Computer wins!")

        elif result == "Draw":
            print("Game Draw!")

        break