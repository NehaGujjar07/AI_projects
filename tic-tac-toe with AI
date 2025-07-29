import tkinter as tk
import random
import math

# Initialize global variables
board = [[" " for _ in range(3)] for _ in range(3)]
difficulty = "Hard"  # Default difficulty level

# Check for a winner
def check_winner():
    for row in board:
        if row == ["X", "X", "X"]:
            return "X"
        if row == ["O", "O", "O"]:
            return "O"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

# Check if the board is full
def is_full():
    for row in board:
        if " " in row:
            return False
    return True

# Evaluate the board for AI decision-making
def evaluate():
    winner = check_winner()
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(depth, is_maximizing, alpha, beta):
    score = evaluate()
    if score in (1, -1) or is_full():
        return score

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(depth + 1, False, alpha, beta)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(depth + 1, True, alpha, beta)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# AI decision-making
def find_best_move():
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(0, False, -math.inf, math.inf)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# AI makes a move based on difficulty
def ai_move():
    if difficulty == "Easy":
        while True:
            row, col = random.randint(0, 2), random.randint(0, 2)
            if board[row][col] == " ":
                return row, col
    elif difficulty == "Medium" and random.random() < 0.5:
        return find_best_move() or (random.randint(0, 2), random.randint(0, 2))
    return find_best_move()

# Handle button clicks
def handle_click(row, col):
    if board[row][col] == " " and check_winner() is None:
        board[row][col] = "X"
        buttons[row][col].config(text="X", state=tk.DISABLED)
        if check_winner() == "X":
            result_label.config(text="You win!", fg="blue")
            disable_all_buttons()
            return
        if is_full():
            result_label.config(text="It's a draw!", fg="orange")
            return

        # AI move
        ai_row, ai_col = ai_move()
        board[ai_row][ai_col] = "O"
        buttons[ai_row][ai_col].config(text="O", state=tk.DISABLED)
        if check_winner() == "O":
            result_label.config(text="AI wins!", fg="red")
            disable_all_buttons()
            return
        if is_full():
            result_label.config(text="It's a draw!", fg="orange")

# Disable all buttons
def disable_all_buttons():
    for row in buttons:
        for button in row:
            button.config(state=tk.DISABLED)

# Reset the game
def reset_game():
    global board
    board = [[" " for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button.config(text="", state=tk.NORMAL)
    result_label.config(text="Your turn!", fg="black")

# Set difficulty and start the game
def start_game(selected_difficulty):
    global difficulty
    difficulty = selected_difficulty
    difficulty_frame.pack_forget()
    game_frame.pack()

# Create the GUI
root = tk.Tk()
root.title("Advanced Tic-Tac-Toe AI")

# Difficulty selection screen
difficulty_frame = tk.Frame(root)
difficulty_label = tk.Label(difficulty_frame, text="Select Difficulty:", font=("Arial", 16))
difficulty_label.pack(pady=10)

for level in ["Easy", "Medium", "Hard"]:
    tk.Button(difficulty_frame, text=level, font=("Arial", 14),
              command=lambda lvl=level: start_game(lvl)).pack(pady=5)

difficulty_frame.pack()

# Game screen
game_frame = tk.Frame(root)
buttons = [[tk.Button(game_frame, text="", font=("Arial", 24), width=5, height=2,
                      command=lambda row=i, col=j: handle_click(row, col))
            for j in range(3)] for i in range(3)]

for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        button.grid(row=i, column=j)

result_label = tk.Label(game_frame, text="Your turn!", font=("Arial", 16))
result_label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(game_frame, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

root.mainloop()
