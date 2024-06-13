import tkinter as tk
from tkinter import messagebox
import random

# Function to start a new game
def start_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess_entry.delete(0, tk.END)
    result_label.config(text="")

# Function to check the user's guess
def check_guess(event=None):
    try:
        guess = int(guess_entry.get())
        global attempts
        attempts += 1

        if guess < number_to_guess:
            result_label.config(text="Too low! Try again.")
        elif guess > number_to_guess:
            result_label.config(text="Too high! Try again.")
        else:
            result_label.config(text=f"Correct! It took you {attempts} attempts.")
            messagebox.showinfo("Congratulations", f"You guessed the number in {attempts} attempts!")
            start_game()  # Start a new game after correct guess

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")

# Initialize the main application window
root = tk.Tk()
root.geometry("800x500")
root.title("Number Guessing Game")
root.configure(bg="black")

# Create and place the widgets using pack with pady=10
instructions_label = tk.Label(root, text="Guess the number between 1 and 100", bg="white", font=(20))
instructions_label.pack(pady=10)

guess_entry = tk.Entry(root, width=20, font=(20))
guess_entry.pack(pady=10)
guess_entry.bind('<Return>', check_guess)

check_button = tk.Button(root, text="Check Guess", command=check_guess, bg="white", font=(20))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman",40), bg="black", fg="white")
result_label.pack(pady=10)

# Start a new game
start_game()

# Start the Tkinter event loop
root.mainloop()