from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QMessageBox
import sys
##########################################################################################################
class tik_tok_to(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("tik tok to")
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
##########################################################################################################
        self.score_X = 0
        self.score_O = 0
##########################################################################################################
        self.buttons = []
        for i in range(9):
            button = QPushButton("", self)
            button.setFixedSize(100, 100)
            button.setStyleSheet("font-size: 40px;")
            self.buttons.append(button)
##########################################################################################################
        grid = QGridLayout()
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)
        k = 0
        self.label_score_X = QLabel(f"X   :  {self.score_X}", self)
        self.label_score_O = QLabel(f"O   :  {self.score_O}", self)
        grid.addWidget(self.label_score_X, 4, 1)
        grid.addWidget(self.label_score_O, 3, 1)
        for i in range(3):
            for j in range(3):
                grid.addWidget(self.buttons[k], i, j)
                k += 1
        main_widget.setLayout(grid)
##########################################################################################################
        self.current_player = "X"
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.gameover = False
##########################################################################################################
        for button in self.buttons:
            button.clicked.connect(self.button_clicked)
##########################################################################################################
        # Add a reset button to the main window
        self.reset_button = QPushButton("Play Again", self)
        self.reset_button.hide()
        self.reset_button.clicked.connect(self.reset_game)
        grid.addWidget(self.reset_button, 5, 0, 1, 3)
##########################################################################################################
    def button_clicked(self):
        if not self.gameover:
            button = self.sender()
            index = self.buttons.index(button)

            if self.board[index] == "":
                self.board[index] = self.current_player
                button.setText(self.current_player)
                if self.current_player == "X":
                    button.setStyleSheet("background-color: red")
                else:
                    button.setStyleSheet("background-color: green")
                self.check_winner()
                self.change_player()
                self.check_draw()
##########################################################################################################
    def check_draw(self):
        if not "" in self.board and not self.gameover:
            self.reset_game()
            QMessageBox.information(self, "Game Over", "The game is a draw.")
##########################################################################################################
    def change_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"
##########################################################################################################
    def check_winner(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                                [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                [0, 4, 8], [2, 4, 6]]
        
        for check in winning_combinations:
            if self.board[check[0]] != "" and self.board[check[0]] == self.board[check[1]] == self.board[check[2]]:
                self.gameover = True
                winner = self.board[check[0]]
                print(f"{winner} wins!")

                if winner == "O":
                    self.score_O += 1
                else:
                    self.score_X += 1
                    # Hide the buttons
                
                for button in self.buttons:
                    button.setEnabled(False)

                # Show the reset button when a player wins
                self.reset_button.show()
                break
##########################################################################################################
    def reset_game(self):
        # Reset the board and update the buttons
        self.current_player = "X"
        self.board = ["", "", "", "", "", "", "", "", ""]
        self.gameover = False

        for button in self.buttons:
            button.setText("")
            button.setEnabled(True)
            button.setStyleSheet("")

        # Hide the reset button again
        self.reset_button.hide()

        # Update the scores labels
        self.label_score_X.setText(f"X   :  {self.score_X}")
        self.label_score_O.setText(f"O   :  {self.score_O}")

##########################################################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    tik_tok_to = tik_tok_to()
    tik_tok_to.show()
    sys.exit(app.exec())
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################