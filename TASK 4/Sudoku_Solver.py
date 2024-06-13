import tkinter as tk
from tkinter import messagebox

# Sudoku solving using backtracking
def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num or board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True

def solve_sudoku(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def display_board(board):
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                cells[i][j].insert(0, str(board[i][j]))
            cells[i][j].config(fg="black")

def solve():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = cells[i][j].get()
            row.append(int(value) if value.isdigit() else 0)
        board.append(row)
    if solve_sudoku(board):
        display_board(board)
    else:
        messagebox.showerror("Error", "No solution exists for the given Sudoku.")

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def focus_prev_widget(event):
    event.widget.tk_focusPrev().focus()
    return("break")

def move_up(event):
    row, col = event.widget.grid_info()['row'], event.widget.grid_info()['column']
    if row > 0:
        cells[row - 1][col].focus()
    return("break")

def move_down(event):
    row, col = event.widget.grid_info()['row'], event.widget.grid_info()['column']
    if row < 8:
        cells[row + 1][col].focus()
    return("break")

def move_left(event):
    row, col = event.widget.grid_info()['row'], event.widget.grid_info()['column']
    if col > 0:
        cells[row][col - 1].focus()
    return("break")

def move_right(event):
    row, col = event.widget.grid_info()['row'], event.widget.grid_info()['column']
    if col < 8:
        cells[row][col + 1].focus()
    return("break")

# Initialize main application window
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("800x700")
root.configure(bg="black")

title_label = tk.Label(root, text="Sudoku Solver", font=("Helvetica", 20), bg="black", fg="white")
title_label.pack(pady=10)

grid_frame = tk.Frame(root, bg="black")
grid_frame.pack(pady=10)

cells = []
for i in range(9):
    row = []
    for j in range(9):
        entry = tk.Entry(grid_frame, width=2, font=("Helvetica", 20), justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5, ipadx=5, ipady=5)
        entry.bind("<Return>", focus_next_widget)
        entry.bind("<Up>", move_up)
        entry.bind("<Down>", move_down)
        entry.bind("<Left>", move_left)
        entry.bind("<Right>", move_right)
        row.append(entry)
    cells.append(row)

solve_button = tk.Button(root, text="Solve", command=solve, bg="lightgray", font=("Helvetica", 20))
solve_button.pack(pady=10)

root.mainloop()