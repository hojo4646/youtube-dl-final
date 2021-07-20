import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from gui import Ui_MainWindow
import youtube_dl as ydl


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ydl_opts = {}
        self.button_url_download.clicked.connect(self.download_url)
        

    def get_url(self):
        return self.input_url.text()

    def test(self):
        print(self.get_url())

    def download_url(self):
        with ydl.YoutubeDL(self.ydl_opts) as yt:
            yt.download([self.get_url()])

    def get_url_info(self):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())