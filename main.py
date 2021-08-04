import sys
import os
import progressbar
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox, QWidget, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from gui import Ui_MainWindow
import youtube_dl as ydl
from threading import Thread
import datetime
from PIL import Image
import io
import requests
import matplotlib.pyplot as plt  #remove later 
import wget

BIN = 'bin'

class Progress(QWidget,progressbar.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.progress = Progress()
        self.progressBar = self.progress.progressBar


        # Connect the download button to the "download_button"
        self.button_url_download.clicked.connect(self.download_button)
        # Connect the url input box to the boolean function that flips the "download_info" thread on and off
        self.input_url.textChanged.connect(self.call_info_thread)

        self.button_thumbnail_download.clicked.connect(self.download_thumbnail)
        
        # Grab video formats from combo box
        self.video_formats = [self.combo_video_formats.itemText(i) for i in range(self.combo_video_formats.count())]

        # Grab audio formats from combo box
        self.audio_formats = [self.combo_audio_formats.itemText(i) for i in range(self.combo_audio_formats.count())]
        # Check Audio Only Checkbox
        self.check_audioonly.toggled.connect(self.toggle_formats)


        # The Variable needInfo, used to test if the line has changed without freezing
        self.needInfo = False

        # Thread that handles getting the info from a video without causing GUI to freeze
        self.info_thread = Thread(target=self.live_info_thread)
        self.info_thread.setDaemon(True) # Die on main Death
        self.info_thread.start()

        self.info = {}
        self.filename = ''
        self.info_ydl_opts = {
            'progress_hooks': [self.progress_hook]
        }
        self.video_ydl_opts = {
            'format': 'best',
            'ffmpeg_location': BIN,
            'progress_hooks': [self.progress_hook],
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': self.combo_video_formats.currentText(),
        }],
        }
        self.audio_ydl_opts = {
            'format': 'bestaudio/best',
            'ffmpeg_location': BIN,
            'progress_hooks': [self.progress_hook],
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': self.combo_audio_formats.currentText(),
                'preferredquality': '192',
        }],
        }

        self.download_options = {

        }
        self.thumbnail_options = {
            "writethumbnail": ""
        }

    def toggle_formats(self):
        if self.combo_video_formats.isHidden():
            self.combo_video_formats.show()
        else:
            self.combo_video_formats.hide()

    # Test Function, no one purpose, change as needed to test things
    def test(self):
        pass
    
    def set_folder(self):
        self.label_var_folder.setText(self.filename.split('/')[:-2])

    def download_button(self):
        if self.check_audioonly.isChecked() == False:
            self.filename = self.get_vid_save_file()
            if self.filename != '':
                self.download_thread_maker(self.download_vid)
                self.progress.show()
        else:
            self.filename = self.get_audio_save_file()
            if self.filename != '':
                self.download_thread_maker(self.download_audio)
                self.progress.show()

    def download_thumbnail(self):
        
        
        pass 

    def download_thread_maker(self,x):
        self.download_thread = Thread(target=x)
        self.download_thread.setDaemon(True) # Die on main Death
        self.download_thread.start()

    # Get input_url text
    def get_url(self):
        return self.input_url.text()

    

    # Download the URL as Audio
    def download_audio(self):
        self.audio_ydl_opts['postprocessors'][0]['preferredcodec'] = self.combo_audio_formats.currentText()
        self.audio_ydl_opts['outtmpl'] = self.filename
        with ydl.YoutubeDL(self.audio_ydl_opts) as yt:
            yt.download([self.get_url()])
            self.set_folder()
        

    # Download the URL as Video
    def download_vid(self):
        self.video_ydl_opts['postprocessors'][0]['preferedformat'] = self.combo_video_formats.currentText()
        self.video_ydl_opts['outtmpl'] = self.filename
        with ydl.YoutubeDL(self.video_ydl_opts) as yt:
            yt.download([self.get_url()])
            self.set_folder()

    # Link to the "if text edited" signal, acting as a link to the "live_info_thread" which 
    # runs the "download_info" method on its own thread, preventing lag from the command being run every keystroke when
    # connected to the "if text edited" signal directly  
    def call_info_thread(self):
        self.needInfo = True
        
    def get_vid_save_file(self):
        name = QFileDialog.getSaveFileName(self, 'Save File',str(self.info['title']+'.'+self.combo_video_formats.currentText()),'.'+self.combo_video_formats.currentText())
        
        return name[0]
    
    def get_audio_save_file(self):
        name = QFileDialog.getSaveFileName(self, 'Save File',str(self.info['title']+'.'+self.combo_audio_formats.currentText()),'.'+self.combo_audio_formats.currentText())
        
        return name[0]

    def progress_hook(self,x):
        pass
        print(x['status'])
        if x['status'] == 'finished':
            #file_tuple = os.path.split(os.path.abspath(x['filename']))
            #print("Done downloading {}".format(file_tuple[1]))
            self.progress.hide()
            self.progressBar.setValue(0)
        if x['status'] == 'downloading':
            p = x['_percent_str']
            p = p.replace('%','')
            self.progressBar.setValue(float(p))
            #print(x['filename'], x['_percent_str'], x['_eta_str'])

    # Receive the entire dictionary of information from the web address for use in display frame
    def download_info(self):
        with ydl.YoutubeDL(self.info_ydl_opts) as yt:
            try:
                return yt.extract_info(self.get_url(),download=False)
            except Exception as e:
                print(e)
    
    
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
            self.info = self.download_info()
            # Get Thumbnail preview
            self.get_thumbnail_preview(self.info['thumbnails'][0]['url'])
            self.button_thumbnail_download.setEnabled(True)
            # Get Video Name
            self.label_var_name.setText(self.info['title'])
            # Get Video Length
            self.label_var_duration.setText(str(datetime.timedelta(seconds=self.info['duration'])))
            # Get Video Description
            self.label_var_description.setText(self.info['description'])
        except Exception as e:
            print(e)
        
    # Retrieve the thumbnail via the url provided in the info dictionary, 
    # and display it to the proper label as a pixmap
    def get_thumbnail_preview(self,url):
        # Convert "Image" object to a BytesIO object, to then be converted into/return a pixmap
        def img2pixmap(img):
            bytes_img = io.BytesIO()
            img.save(bytes_img, format='JPEG')
            qimg = QImage()
            qimg.loadFromData(bytes_img.getvalue())
            self.img_thumbnail_display.setPixmap(QPixmap.fromImage(qimg))
        # Get link from url
        data = requests.get(url).content
        # Save link in Image
        img = Image.open(io.BytesIO(data))
        # Send Image to function to be converted to pixmap
        img2pixmap(img)

    def download_thumbnail(self):
        name = QFileDialog.getSaveFileName(self, 'Save File',str(self.info['title']+'.png'),'.'+self.combo_video_formats.currentText())
        
        wget.download(url=self.info['thumbnails'][-1]['url'],out=name[0])
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())