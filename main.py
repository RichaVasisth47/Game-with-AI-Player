import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
root.title("Tic Tac Toe vs Smart AI")
root.geometry("300x350")
root.config(bg="#1a1a1a")

board = [" " for _ in range(9)]
buttons = []


def check_winner(b, player):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    for w in wins:
        if b[w[0]] == player and b[w[1]] == player and b[w[2]] == player:
            return True
    return False


def reset_board():
    global board
    board = [" " for _ in range(9)]
    for btn in buttons:
        btn.config(text="")


def ai_move():
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    if not empty_spots:
        return

    # Step 1: Check if AI can win in the next move
    for i in empty_spots:
        board[i] = "O"
        if check_winner(board, "O"):
            buttons[i].config(text="O", fg="#ff4d4d")
            messagebox.showinfo("Game Over", "AI won the game! Better luck next time.")
            reset_board()
            return
        board[i] = " "

    # Step 2: Check if Player can win in the next move, and block them
    for i in empty_spots:
        board[i] = "X"
        if check_winner(board, "X"):
            board[i] = "O"
            buttons[i].config(text="O", fg="#ff4d4d")
            if " " not in board:
                messagebox.showinfo("Game Over", "It's a draw!")
                reset_board()
            return
        board[i] = " "

    # Step 3: Take center if available
    if board[4] == " ":
        move = 4
    else:
        # Step 4: Otherwise pick a random available spot
        move = random.choice(empty_spots)

    board[move] = "O"
    buttons[move].config(text="O", fg="#ff4d4d")

    if check_winner(board, "O"):
        messagebox.showinfo("Game Over", "AI won the game! Better luck next time.")
        reset_board()
    elif " " not in board:
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_board()


def button_click(index):
    if board[index] == " ":
        board[index] = "X"
        buttons[index].config(text="X", fg="#8B4513")  # Brown color for Player

        if check_winner(board, "X"):
            messagebox.showinfo("Game Over", "Congratulations! You won the game!")
            reset_board()
            return
        elif " " not in board:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_board()
            return

        # AI turn
        root.after(400, ai_move)


# Grid layout for buttons
for i in range(9):
    btn = tk.Button(root, text="", font=('Arial', 20, 'bold'), width=5, height=2,
                    bg="#2a2a2a", fg="#ffffff", activebackground="#3a3a3a",
                    command=lambda i=i: button_click(i))
    btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(btn)

root.mainloop()