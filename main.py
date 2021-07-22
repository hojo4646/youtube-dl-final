import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from gui import Ui_MainWindow
import youtube_dl as ydl
from threading import Thread
import time
import datetime
from PIL import Image
import io
import requests
import matplotlib.pyplot as plt  #remove later 


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.ydl_opts = {}

        # Connect the download button to the "download_url"
        self.button_url_download.clicked.connect(self.download_url)
        # Connect the url input box to the boolean function that flips the "download_info" thread on and off
        self.input_url.textChanged.connect(self.call_info_thread)
        
        # The Variable needInfo, used to test if the line has changed without freezing
        self.needInfo = False

        # Thread that handles getting the info from a video without causing GUI to freeze
        self.info_thread = Thread(target=self.live_info_thread)
        self.info_thread.setDaemon(True) # Die on main Death
        self.info_thread.start()
        
        
    # Get input_url text
    def get_url(self):
        return self.input_url.text()

    # Test Function, no one purpose, change as needed to test things
    def test(self):
        pass

    # Download the URL
    def download_url(self):
        with ydl.YoutubeDL(self.ydl_opts) as yt:
            yt.download([self.get_url()])

    # Link to the "if text edited" signal, acting as a link to the "live_info_thread" which 
    # runs the "download_info" method on its own thread, preventing lag from the command being run every keystroke when
    # connected to the "if text edited" signal directly  
    def call_info_thread(self):
        self.needInfo = True
        

    # Receive the entire dictionary of information from the web address for use in display frame
    def download_info(self):
        with ydl.YoutubeDL(self.ydl_opts) as yt:
            try:
                return yt.extract_info(self.get_url(),download=False)
            except Exception as e:
                pass
    
    
    # Forever looping thread to call information gathering 
    def live_info_thread(self):
        while True:
            if self.needInfo == True:
                self.update_info()
                self.needInfo = False


    # Take dictionary from "download_info" and place information into their respective QtLabels. 
    # Also calls "get_thumbnail_preview to display thumbnail preview at the same time as the other information"
    def update_info(self):
        try:
            info = self.download_info()
            # Get Thumbnail preview
            self.img_thumbnail_display.setPixmap(self.get_thumbnail_preview(info['thumbnails'][0]['url']))
            # Get Video Name
            self.label_var_name.setText(info['title'])
            # Get Video Length
            self.label_var_duration.setText(str(datetime.timedelta(seconds=info['duration'])))
            # Get Video Description
            self.label_var_description.setText(info['description'])
        except Exception as e:
            pass
        
    # Retrieve the thumbnail via the url provided in the info dictionary, 
    # and display it to the proper label as a pixmap
    def get_thumbnail_preview(self,url):
        # Convert "Image" object to a BytesIO object, to then be converted into/return a pixmap
        def img2pixmap(img):
            bytes_img = io.BytesIO()
            img.save(bytes_img, format='JPEG')
            qimg = QImage()
            qimg.loadFromData(bytes_img.getvalue())
            return QPixmap.fromImage(qimg)
        # Get link from url
        data = requests.get(url).content
        # Save link in Image
        img = Image.open(io.BytesIO(data))
        # Send Image to function to be converted to pixmap
        img2pixmap(img)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())