import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' ']*9
        self.player = 'X'
        self.buttons = []
        self.game_over = False

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 50), width=4, height=2, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                self.buttons.append(button)

        self.status_label = tk.Label(self.master, text='Player ' + self.player + ' turn', font=('Arial', 20))
        self.status_label.grid(row=3, columnspan=3)

        restart_button = tk.Button(self.master, text='Restart', font=('Arial', 20), command=self.restart)
        restart_button.grid(row=4, columnspan=3)

    def make_move(self, row, col):
        index = row*3 + col
        if not self.game_over and self.board[index] == ' ':
            self.board[index] = self.player
            self.buttons[index].config(text=self.player)
            if self.check_win():
                self.status_label.config(text='Player ' + self.player + ' wins!', fg='green')
                self.game_over = True
            elif ' ' not in self.board:
                self.status_label.config(text='Tie!', fg='orange')
                self.game_over = True
            else:
                self.player = 'O' if self.player == 'X' else 'X'
                self.status_label.config(text='Player ' + self.player + ' turn')

    def check_win(self):
        win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                for i in condition:
                    self.buttons[i].config(fg='red')
                return True
        return False

    def restart(self):
        self.board = [' ']*9
        self.player = 'X'
        self.game_over = False
        for button in self.buttons:
            button.config(text='', fg='black')
        self.status_label.config(text='Player ' + self.player + ' turn', fg='black')

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
