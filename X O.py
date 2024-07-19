import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.player = 'X'
        self.board = [' ']*9
        self.root = tk.Tk()
        self.root.title('X O')
        self.buttons = []
        for i in range(3):
            button_row = []
            for j in range(3):
                
              
              #color 
              
                button = tk.Button(self.root, text='', width=10, height=5,
                                   command=lambda row=i, col=j: self.click(row, col),
                                   bg='purple', fg='black', font=('Arial',20 ))
                button.grid(row=i, column=j)
                button_row.append(button)
            self.buttons.append(button_row)

    def click(self, row, col):
        if self.buttons[row][col]['text'] == '':
            self.buttons[row][col]['text'] = self.player
            self.board[row*3+col] = self.player
            if self.check_winner():
                messagebox.showinfo('Game Over', 'Player '+self.player+' wins!')
                self.root.destroy()
            elif self.check_tie():
                messagebox.showinfo('Game Over', 'Tie game!')
                self.root.destroy()
            else:
                self.player = 'O' if self.player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != ' ':
                return True
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != ' ':
                return True
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        if self.board[2] == self.board[4] == self.board[6] != ' ':
            return True
        return False

    def check_tie(self):
        return ' ' not in self.board

    def play(self):
        self.root.mainloop()

game = TicTacToe()
game.play()