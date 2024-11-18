import tkinter as tk
import random
from tkinter import messagebox

def check_guess():
    global guess_attempts  # it will allow to update the guesattempt
    guess = int(entry.get())  # it use to take the input from funtion to button
    guess_attempts += 1

    if guess > number:
        result_label.config(text="Your guess is too high. Try a smaller number.") #
    elif guess < number:
        result_label.config(text="Your guess is too low. Try a higher number.")
    else:
        messagebox.showinfo("Congratulations!", f"You won in {guess_attempts} attempts!")
        reset_game()

    if guess_attempts >= 4 and guess != number:
        messagebox.showinfo("Game Over", f"The correct number was {number}.")
        reset_game()

def reset_game():                         # reset function for reseting game after ending first time
    global number, guess_attempts
    number = random.randint(1, 13)
    guess_attempts = 0
    entry.delete(0, tk.END)             # it will Clears the entry field.
    result_label.config(text="")

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x300")

# Initialize game variables
number = random.randint(1, 13)
guess_attempts = 0

# Create and place widgets
tk.Label(root, text="Guess a Number between 1 and 13").pack(pady=10)

entry = tk.Entry(root)          # Creates an entry widget for user input.
entry.pack(pady=5)

tk.Button(root, text="Submit Guess", command=check_guess,bg = "orange ").pack(pady=5)

result_label = tk.Label(root, text="")     # the text which we want to configurate with if elife conditon
result_label.pack(pady=5)

# Start the main event loop
root.mainloop()