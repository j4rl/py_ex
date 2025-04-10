import customtkinter as ctk
from tkinter import messagebox
import random
import numpy as np
class TicTacToeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("400x400")
        self.reset_game_state()
        self.create_widgets()

    def reset_game_state(self):
        self.board = np.full((3, 3), -1)
        self.human_symbol = 1  # Default to X
        self.computer_symbol = 0
        self.current_turn = 1  # X always starts
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

    def create_widgets(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = ctk.CTkButton(
                    self, text="", width=100, height=100,
                    command=lambda x=i, y=j: self.handle_human_move(x, y)
                )
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.restart_button = ctk.CTkButton(self, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=3, column=0, columnspan=3, pady=10)
        self.prompt_symbol_selection()

    def prompt_symbol_selection(self):
        def set_symbol(symbol):
            self.human_symbol = 1 if symbol == "X" else 0
            self.computer_symbol = 0 if symbol == "X" else 1
            self.current_turn = 1  # X always starts
            symbol_window.destroy()
            if self.current_turn == self.computer_symbol:
                self.after(100, self.handle_computer_move)

        symbol_window = ctk.CTkToplevel(self)
        symbol_window.grab_set()  # Make the dialog modal
        ctk.CTkLabel(symbol_window, text="Choose your symbol:").pack(pady=10)
        ctk.CTkButton(symbol_window, text="X", command=lambda: set_symbol("X")).pack(side="left", padx=10)
        ctk.CTkButton(symbol_window, text="O", command=lambda: set_symbol("O")).pack(side="right", padx=10)

    def handle_human_move(self, x, y):
        if self.is_valid_move(x, y, self.human_symbol):
            self.update_board(x, y, self.human_symbol)
            if self.check_game_status(self.human_symbol, "You win!"):
                return
            self.current_turn = self.computer_symbol
            self.handle_computer_move()

    def handle_computer_move(self):
        move = self.find_best_move()
        if move:
            x, y = move
            self.update_board(x, y, self.computer_symbol)
            if self.check_game_status(self.computer_symbol, "Computer wins!"):
                return
            self.current_turn = self.human_symbol

    def find_best_move(self):
        best_score = -float("inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == -1:
                    self.board[i, j] = self.computer_symbol
                    score = self.minimax(0, False)
                    self.board[i, j] = -1
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move

    def minimax(self, depth, is_maximizing):
        if self.check_winner(self.computer_symbol):
            return 1
        if self.check_winner(self.human_symbol):
            return -1
        if np.all(self.board != -1):
            return 0

        best_score = -float("inf") if is_maximizing else float("inf")
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == -1:
                    self.board[i, j] = self.computer_symbol if is_maximizing else self.human_symbol
                    score = self.minimax(depth + 1, not is_maximizing)
                    self.board[i, j] = -1
                    best_score = max(best_score, score) if is_maximizing else min(best_score, score)
        return best_score

    def is_valid_move(self, x, y, symbol):
        return self.board[x, y] == -1 and self.current_turn == symbol

    def update_board(self, x, y, symbol):
        self.board[x, y] = symbol
        self.buttons[x][y].configure(
            text="X" if symbol == 1 else "O", state="disabled"
        )

    def check_game_status(self, symbol, message):
        if self.check_winner(symbol):
            messagebox.showinfo("Game Over", message)
            self.disable_all_buttons()
            return True
        if np.all(self.board != -1):
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        return False

    def check_winner(self, symbol):
        for i in range(3):
            if np.all(self.board[i, :] == symbol) or np.all(self.board[:, i] == symbol):
                return True
        if self.board[0, 0] == symbol and self.board[1, 1] == symbol and self.board[2, 2] == symbol:
            return True
        if self.board[0, 2] == symbol and self.board[1, 1] == symbol and self.board[2, 0] == symbol:
            return True
        return False

    def disable_all_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(state="disabled")

    def restart_game(self):
        self.reset_game_state()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].configure(text="", state="normal")
        self.prompt_symbol_selection()


if __name__ == "__main__":
    app = TicTacToeApp()
    app.mainloop()


