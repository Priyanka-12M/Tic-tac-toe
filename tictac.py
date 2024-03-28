def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    current_player = players[0]
    moves = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while moves < 9:
        row = int(input(f"Player {current_player}, enter row number (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column number (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move! Try again.")
            continue

        board[row][col] = current_player
        moves += 1
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        current_player = players[moves % 2]

    if moves == 9:
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
