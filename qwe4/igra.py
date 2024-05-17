import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QInputDialog
from PySide6.QtGui import QIntValidator

class Player:
    def __init__(self, name):
        self.name = name
        self.stones = 0

class PseudonymGame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Игра "Псевдоним"')

        self.stones_label = QLabel('Количество камней на столе: ')
        self.stones_count = QLineEdit(self)
        self.stones_count.setValidator(QIntValidator())
        self.stones_count.setText('20')  # Начальное количество камней
        self.stones_count.setMaxLength(2)  # Ограничение на количество цифр

        self.player1 = Player('Victor')
        self.player2 = Player('Computer')

        self.take_stones_button = QPushButton('Взять камни', self)
        self.take_stones_button.clicked.connect(lambda: self.takeStones(self.player1))  # Первый игрок начинает

        vbox = QVBoxLayout(self)
        vbox.addWidget(self.stones_label)
        vbox.addWidget(self.stones_count)
        vbox.addWidget(self.take_stones_button)

        self.setGeometry(300, 300, 300, 150)

    def takeStones(self, current_player):
        current_stones = int(self.stones_count.text())
        taken = self.showInputDialog(current_stones, current_player) if current_player == self.player1 else self.turn_AI(current_stones)
        if taken:
            remaining_stones = current_stones - taken
            current_player.stones += taken
            if remaining_stones < 0:
                remaining_stones = 0
            self.stones_count.setText(str(remaining_stones))
            if remaining_stones <= 0:
                self.showWinner(current_player)
            else:
                next_player = self.player2 if current_player == self.player1 else self.player1
                self.takeStones(next_player)

    def turn_AI(self, current_stones):
        taken = min(current_stones, 3)
        return taken

    def showInputDialog(self, remaining_stones, current_player):
        num, ok = QInputDialog.getInt(self, f'Игрок {current_player.name}', f'Сколько камней взять (не более 3)?\nКамней на столе: {remaining_stones}', 1, 1, 3)
        if ok:
            return num if num <= remaining_stones else self.showInputDialog(remaining_stones, current_player)
        else:
            return 0

    def clearGameData(self):
        self.stones_count.clear()
        self.player1.stones = 0
        self.player2.stones = 0

    def showWinner(self, player):
        QMessageBox.information(self, 'Winner', f'{player.name} - win!!!')
        self.clearGameData()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = PseudonymGame()
    game.show()
    sys.exit(app.exec())