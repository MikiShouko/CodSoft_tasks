import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the game result
def play_game(player_choice):
    global user_score, computer_score
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""
    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Scissors" and computer_choice == "Paper") or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):
        result = "You win!"
        user_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    computer_choice_label.config(text=f"Computer chose: {computer_choice}")
    result_label.config(text=result)
    update_score()

# Function to update the score labels
def update_score():
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Create a label for the player's choice
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:")
label.pack()

# Create buttons for Rock, Paper, and Scissors
rock_button = tk.Button(window, text="Rock", command=lambda: play_game("Rock"))
paper_button = tk.Button(window, text="Paper", command=lambda: play_game("Paper"))
scissors_button = tk.Button(window, text="Scissors", command=lambda: play_game("Scissors"))

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Create labels for computer choice and game result
computer_choice_label = tk.Label(window, text="")
result_label = tk.Label(window, text="")

computer_choice_label.pack()
result_label.pack()

# Create labels for user and computer scores
user_score_label = tk.Label(window, text="Your Score: 0")
computer_score_label = tk.Label(window, text="Computer Score: 0")

user_score_label.pack()
computer_score_label.pack()

# Start the Tkinter main loop
window.mainloop()
