import sys


def create_board():
    return [" "] * 9


def display_board(board):
    print()
    print("  Current Board:          Position Guide:")
    print()
    for row in range(3):
        cells = []
        for col in range(3):
            idx = row * 3 + col
            cells.append(f" {board[idx]} ")
        board_row = "|".join(cells)
        
        guide_cells = []
        for col in range(3):
            idx = row * 3 + col
            if board[idx] == " ":
                guide_cells.append(f" {idx} ")
            else:
                guide_cells.append(f" {board[idx]} ")
        guide_row = "|".join(guide_cells)
        
        print(f"  {board_row}         {guide_row}")
        
        if row < 2:
            print(f"  -----------         -----------")
    print()


WINNING_COMBINATIONS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


def check_winner(board, player):
    for combo in WINNING_COMBINATIONS:
        if all(board[i] == player for i in combo):
            return True
    return False


def check_draw(board):
    return " " not in board and not check_winner(board, "X") and not check_winner(board, "O")


def get_available_moves(board):
    return [i for i in range(9) if board[i] == " "]


def is_game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or check_draw(board)


def minimax(board, depth, is_maximizing):
    if check_winner(board, "O"):
        return 10 - depth
    if check_winner(board, "X"):
        return depth - 10
    if check_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, depth + 1, False)
            board[move] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, depth + 1, True)
            board[move] = " "
            best_score = min(score, best_score)
        return best_score


def get_ai_move(board):
    best_score = -float("inf")
    best_move = None
    
    for move in get_available_moves(board):
        board[move] = "O"
        score = minimax(board, 0, False)
        board[move] = " "
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move


def get_human_move(board):
    while True:
        try:
            move = input("Your move (0-8): ").strip()
            move = int(move)
            
            if move < 0 or move > 8:
                print("Invalid! Please enter a number between 0 and 8.")
                continue
            
            if board[move] != " ":
                print("That cell is already taken! Choose an empty cell.")
                continue
            
            return move
            
        except ValueError:
            print("Invalid input! Please enter a number (0-8).")
        except (EOFError, KeyboardInterrupt):
            print("\nGame ended by user.")
            sys.exit(0)


def play_game():
    print("=" * 50)
    print("  TIC-TAC-TOE with MINIMAX AI")
    print("=" * 50)
    print()
    print("You are 'X' and the AI is 'O'.")
    print("You go first! Enter a position number (0-8).")
    print("The AI uses Minimax - it plays perfectly!")
    
    board = create_board()
    display_board(board)
    
    while True:
        print("--- Your Turn (X) ---")
        human_move = get_human_move(board)
        board[human_move] = "X"
        display_board(board)
        
        if check_winner(board, "X"):
            print("Congratulations! You won! (This shouldn't happen against Minimax!)")
            break
        if check_draw(board):
            print("It's a draw! Well played!")
            break
        
        print("--- AI's Turn (O) ---")
        print("AI is thinking...")
        ai_move = get_ai_move(board)
        board[ai_move] = "O"
        print(f"AI plays at position {ai_move}")
        display_board(board)
        
        if check_winner(board, "O"):
            print("The AI wins! Better luck next time!")
            break
        if check_draw(board):
            print("It's a draw! Well played!")
            break


def main():
    while True:
        play_game()
        print()
        try:
            again = input("Play again? (yes/no): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nThanks for playing!")
            break
        
        if again not in ("yes", "y"):
            print("Thanks for playing! Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
