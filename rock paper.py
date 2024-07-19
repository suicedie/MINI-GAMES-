import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Rock Paper Scissors')

        # Add background canvas with stars animation
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg='black')
        self.canvas.pack()
        self.stars = []
        for i in range(75):
            x = random.randint(1, 400)
            y = random.randint(1, 400)
            self.stars.append(self.canvas.create_oval(x, y, x+2, y+2, fill='white', outline='white'))
        self.animate()

        # Add frame with buttons
        self.button_frame = tk.Frame(self.root, bg='black')
        self.button_frame.pack(pady=20)
        self.buttons = []
        self.buttons.append(tk.Button(self.button_frame, text='Rock', font=('Arial', 14, 'bold'), width=10, bg='gray', fg='white', command=lambda: self.play('rock')))
        self.buttons[-1].pack(side='left', padx=10)
        self.buttons.append(tk.Button(self.button_frame, text='Paper', font=('Arial', 14, 'bold'), width=10, bg='gray', fg='white', command=lambda: self.play('paper')))
        self.buttons[-1].pack(side='left', padx=10)
        self.buttons.append(tk.Button(self.button_frame, text='Scissors', font=('Arial', 14, 'bold'), width=10, bg='gray', fg='white', command=lambda: self.play('scissors')))
        self.buttons[-1].pack(side='left', padx=10)

        # Initialize game state
        self.player_choice = None
        self.computer_choice = None

    def animate(self):
        for star in self.stars:
            dx = random.randint(-1, 1)
            dy = random.randint(-1, 1)
            self.canvas.move(star, dx, dy)
        self.canvas.after(50, self.animate)

    def play(self, player_choice):
        # Update game state
        self.player_choice = player_choice
        self.computer_choice = random.choice(['rock', 'paper', 'scissors'])

        # Determine result
        result = ''
        if self.player_choice == self.computer_choice:
            result = 'Tie!'
        elif self.player_choice == 'rock' and self.computer_choice == 'scissors':
            result = 'You win!'
        elif self.player_choice == 'paper' and self.computer_choice == 'rock':
            result = 'You win!'
        elif self.player_choice == 'scissors' and self.computer_choice == 'paper':
            result = 'You win!'
        else:
            result = 'You lose!'

        # Show result to user
        messagebox.showinfo('Result', f'You chose {self.player_choice}. Computer chose {self.computer_choice}. {result}')

game = RockPaperScissors()
game.root.mainloop()