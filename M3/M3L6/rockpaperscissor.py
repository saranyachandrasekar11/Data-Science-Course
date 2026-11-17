import random
import tkinter as tk

# Global score variables
player_score = 0
computer_score = 0
choices = ["Rock", "Paper", "Scissors"]


# Function to handle each round when a button is clicked
def play_round(player_choice):
    global player_score, computer_score

    # 1. Computer makes a random choice
    computer_choice = random.choice(choices)

    # 2. Conditional statements to decide the winner
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    # 3. Update the GUI labels
    choice_label.config(
        text=f"You chose: {player_choice}  |  Computer chose: {computer_choice}"
    )
    result_label.config(text=result)
    score_label.config(
        text=f"Score — You: {player_score}  |  Computer: {computer_score}"
    )


# Function to reset scores and labels
def reset_game():
    global player_score, computer_score
    player_score = 0
    computer_score = 0
    choice_label.config(text="Make your move below!")
    result_label.config(text="")
    score_label.config(text="Score — You: 0  |  Computer: 0")


# --- GUI Setup using Tkinter ---
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("420x320")
root.resizable(False, False)

# Title Label
title_label = tk.Label(
    root, text="Rock, Paper, Scissors", font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

# Score Display
score_label = tk.Label(
    root, text="Score — You: 0  |  Computer: 0", font=("Arial", 12)
)
score_label.pack(pady=5)

# Choice & Result Display
choice_label = tk.Label(
    root, text="Make your move below!", font=("Arial", 11), fg="#333333"
)
choice_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#0052cc")
result_label.pack(pady=5)

# Frame to hold the three choice buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

# Loop to dynamically create Rock, Paper, and Scissors buttons
for move in choices:
    btn = tk.Button(
        button_frame,
        text=move,
        width=10,
        font=("Arial", 11),
        command=lambda m=move: play_round(m),
    )
    btn.pack(side=tk.LEFT, padx=8)

# Reset Button
reset_btn = tk.Button(
    root, text="Reset Game", font=("Arial", 10), command=reset_game
)
reset_btn.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
