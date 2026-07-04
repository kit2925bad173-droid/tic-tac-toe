import math

# Initialize board
board = [' ' for _ in range(9)]

# Display board
def print_board():
    print()
    for i in range(3):
        print(" " + " | ".join(board[i * 3:(i + 1) * 3]))
        if i < 2:
            print("---+---+---")
    print()

# Position guide
def print_positions():
    print("""
Position Guide:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")

# Check winner
def check_winner(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for combo in win_combinations:
        if all(board[pos] == player for pos in combo):
            return True

    return False

# Check draw
def is_draw():
    return ' ' not in board

# Minimax with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):

    if check_winner('O'):
        return 10 - depth

    if check_winner('X'):
        return depth - 10

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'

                score = minimax(depth + 1, False, alpha, beta)

                board[i] = ' '

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)

                if beta <= alpha:
                    break

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'

                score = minimax(depth + 1, True, alpha, beta)

                board[i] = ' '

                best_score = min(best_score, score)
                beta = min(beta, best_score)

                if beta <= alpha:
                    break

        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            score = minimax(
                0,
                False,
                -math.inf,
                math.inf
            )

            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'
    print(f"AI selected position {best_move + 1}")

# Human Move
def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move] != ' ':
                print("This position is already occupied.")
                continue

            board[move] = 'X'
            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main Game Function
def play_game():

    print("=" * 40)
    print("       TIC-TAC-TOE AI AGENT")
    print("=" * 40)

    print_positions()

    print("Human Player : X")
    print("AI Player    : O")
    print()

    while True:

        # Human Turn
        print_board()
        human_move()

        if check_winner('X'):
            print_board()
            print("Human Player Wins!")
            break

        if is_draw():
            print_board()
            print("The game is a draw.")
            break

        # AI Turn
        ai_move()

        if check_winner('O'):
            print_board()
            print("AI Player Wins!")
            break

        if is_draw():
            print_board()
            print("The game is a draw.")
            break

# Run the Game
if __name__ == "__main__":
    play_game()
