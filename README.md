# Codsoft-project
import tkinter as tk
from random import choice

class RockPaperScissors:
    def _init_(self):
        self.window = tk.Tk()
        self.window.title("Rock-Paper-Scissors")
        self.window.geometry("700x500")
        self.window.configure(background="#f0f0f0")
        self.player_score = 0
        self.computer_score = 0
        self.score_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.score_frame.pack(pady=20)
        self.player_score_label = tk.Label(self.score_frame, text="Player Score: 0", font=("Arial", 24), fg="#00698f")
        self.player_score_label.pack(side=tk.LEFT, padx=20)
        self.computer_score_label = tk.Label(self.score_frame, text="Computer Score: 0", font=("Arial", 24), fg="#00698f")
        self.computer_score_label.pack(side=tk.RIGHT, padx=20)
        self.choice_frame = tk.Frame(self.window, bg="#f0f0f0")
        self.choice_frame.pack(pady=20)
        self.rock_button = tk.Button(self.choice_frame, text="✊", command=lambda: self.play("rock"), font=("Arial", 20), fg="#ff69b4", bg="#f0f0f0", width=5, height=2)
        self.rock_button.pack(side=tk.LEFT, padx=10)
        self.paper_button = tk.Button(self.choice_frame, text="🖐", command=lambda: self.play("paper"), font=("Arial", 20), fg="#34c759", bg="#f0f0f0", width=5, height=2)
        self.paper_button.pack(side=tk.LEFT, padx=10)
        self.scissors_button = tk.Button(self.choice_frame, text="✌", command=lambda: self.play("scissors"), font=("Arial", 20), fg="#ff9900", bg="#f0f0f0", width=5, height=2)
        self.scissors_button.pack(side=tk.LEFT, padx=10)
        self.result_label = tk.Label(self.window, text="", font=("Arial", 18), fg="#00698f")
        self.result_label.pack(pady=20)
    def play(self, player_choice):
        choices = ["rock", "paper", "scissors"]
        computer_choice = choice(choices)
        if player_choice == computer_choice:
            result = "It's a tie!"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            result = "You win!"
            self.player_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        self.result_label.config(text=f"You chose: {'✊' if player_choice == 'rock' else '✂' if player_choice == 'paper' else '✂'}, Computer chose: {'✊' if computer_choice == 'rock' else '✂' if computer_choice == 'paper' else '✂'}, {result}")
        self.player_score_label.config(text=f"Player Score: {self.player_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")
    def run(self):
        self.window.mainloop()

if __name__ == "_main_":
    game = RockPaperScissors()
    game.run()
