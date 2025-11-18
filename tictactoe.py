# --- GLOBAL GAME VARIABLES ---
# The board is a list of 9 elements, initially representing empty spaces.
board = [" " for x in range(9)]
game_active = True
current_player = "X"
winner = None

# --- 1. DISPLAY THE BOARD ---
def display_board():
    """Prints the 3x3 game board to the console."""
    print("-------------")
    # Row 1: Indices 0, 1, 2
    print(f"| {board[0]} | {board[1]} | {board[2]} |")
    print("-------------")
    # Row 2: Indices 3, 4, 5
    print(f"| {board[3]} | {board[4]} | {board[5]} |")
    print("-------------")
    # Row 3: Indices 6, 7, 8
    print(f"| {board[6]} | {board[7]} | {board[8]} |")
    print("-------------")

# --- 2. HANDLE A SINGLE TURN ---
def handle_turn(player):
    """
    Handles a single turn for a given player. 
    Prompts for input and validates the move.
    """
    print(f"\n{player}'s turn.")
    
    # Prompt the player to choose a spot (1-9)
    valid_move = False
    while not valid_move:
        try:
            position = input("Choose a position from 1-9: ")
            
            # Check if input is a digit
            if not position.isdigit():
                print("Invalid input. Please enter a number from 1 to 9.")
                continue

            position = int(position) - 1 # Convert to 0-indexed list position
            
            # Check if position is within bounds (0-8)
            if position not in range(9):
                print("Invalid input. That position is outside the board.")
                continue

            # Check if the spot is already taken
            if board[position] == " ":
                valid_move = True
                board[position] = player
            else:
                print("That spot is already taken. Choose another.")

        except ValueError:
            print("Invalid input. Please enter a number.")

# --- 3. CHECK FOR GAME END CONDITIONS ---

def check_for_win():
    """Checks for a win across rows, columns, and diagonals."""
    global winner
    
    # Define winning combinations (indices of the board list)
    win_conditions = [
        # Rows
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columns
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonals
        (0, 4, 8), (2, 4, 6)
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != " ":
            winner = board[a]
            return True
    return False

def check_for_draw():
    """Checks if all spots are filled (a draw)."""
    # If there are no empty spaces and no winner, it's a draw
    if " " not in board:
        return True
    return False

# --- 4. FLIP PLAYER ---
def flip_player():
    """Switches the current player from X to O or vice versa."""
    global current_player
    current_player = "O" if current_player == "X" else "X"

# --- 5. MAIN GAME FUNCTION ---
def play_game():
    """Main function to control the flow of the game."""
    global game_active, winner
    
    # Initial board display
    print("Welcome to Tic-Tac-Toe!")
    display_board()
    
    # Main game loop
    while game_active:
        
        # Handle a turn for the current player
        handle_turn(current_player)
        
        # Check if the game has ended after the move
        if check_for_win():
            game_active = False
            break
        
        if check_for_draw():
            game_active = False
            break
            
        # Display the board after the successful move
        display_board()

        # Switch to the other player
        flip_player()

    # Game finished: print final result
    print("\n--- GAME OVER ---")
    display_board()
    
    if winner:
        print(f"The winner is {winner}!")
    else:
        print("It's a Draw!")

# Start the game
if __name__ == "__main__":
    play_game()
