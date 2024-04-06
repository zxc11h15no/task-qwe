import os
import sys
import random
import pygame
from PyQt6 import QtWidgets
from player_form import Ui_MainWindow as Ui_PlayerForm

class PlayerForm(QtWidgets.QMainWindow, Ui_PlayerForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.update_list)
        self.pushButton_4.clicked.connect(self.shuffle_list)
        self.pushButton.clicked.connect(self.play_music)
        self.pushButton_2.clicked.connect(self.pause_or_unpause_music)
        self.dir = ""
        self.music_files = []

    def update_list(self):
        self.listWidget.clear()
        self.music_files.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Selected")
        if directory:
            for file_name in os.listdir(directory):
                if file_name.endswith(".mp3"):
                    self.listWidget.addItem(file_name)
                    self.music_files.append(os.path.join(directory, file_name))
            self.dir = directory

    def shuffle_list(self):
        random.shuffle(self.music_files)

    def play_music(self):
        if self.music_files:
            file_path = self.music_files[self.listWidget.currentRow()]
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()

    def pause_or_unpause_music(self):
        if pygame.mixer.music.get_busy() and pygame.mixer.music.get_pos() > 0:
            pygame.mixer.music.pause()
            self.pushButton_2.setText("Play")
        else:
            pygame.mixer.music.unpause()
            self.pushButton_2.setText("Pause")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    playerform = PlayerForm()
    playerform.show()
    sys.exit(app.exec())