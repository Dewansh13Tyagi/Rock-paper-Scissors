import tkinter as tk
import random

# Choices
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    comp_choice = random.choice(choices)

    # Determine winner
    if user_choice == comp_choice:
        result_text.set(f"Both chose {user_choice.capitalize()} → It's a Tie!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        user_score += 1
        result_text.set(f"You chose {user_choice.capitalize()}, Computer chose {comp_choice.capitalize()} → 🎉 You Win!")
    else:
        computer_score += 1
        result_text.set(f"You chose {user_choice.capitalize()}, Computer chose {comp_choice.capitalize()} → 💻 Computer Wins!")

    score_text.set(f"Score → You: {user_score} | Computer: {computer_score}")

def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    score_text.set("Score → You: 0 | Computer: 0")
    result_text.set("Make your move!")

# GUI window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")

title_label = tk.Label(root, text="Rock, Paper, Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

# Result display
result_text = tk.StringVar()
result_text.set("Make your move!")
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 12), wraplength=350, justify="center")
result_label.pack(pady=10)

# Score display
score_text = tk.StringVar()
score_text.set("Score → You: 0 | Computer: 0")
score_label = tk.Label(root, textvariable=score_text, font=("Arial", 12))
score_label.pack(pady=5)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors")).grid(row=0, column=2, padx=5)

# Reset button
tk.Button(root, text="Reset Scores", command=reset_scores).pack(pady=10)

# Exit button
tk.Button(root, text="Exit Game", command=root.quit).pack()

root.mainloop()
