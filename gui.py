# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(687, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 691, 411))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.input_url = QtWidgets.QLineEdit(self.tab)
        self.input_url.setGeometry(QtCore.QRect(140, 210, 321, 21))
        self.input_url.setText("")
        self.input_url.setObjectName("input_url")
        self.button_url_download = QtWidgets.QPushButton(self.tab)
        self.button_url_download.setGeometry(QtCore.QRect(470, 210, 75, 23))
        self.button_url_download.setObjectName("button_url_download")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(0, 20, 681, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_videoinfo = QtWidgets.QLabel(self.frame)
        self.label_videoinfo.setGeometry(QtCore.QRect(20, 0, 61, 16))
        self.label_videoinfo.setObjectName("label_videoinfo")
        self.label_info_name = QtWidgets.QLabel(self.frame)
        self.label_info_name.setGeometry(QtCore.QRect(20, 26, 51, 20))
        self.label_info_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_info_name.setObjectName("label_info_name")
        self.label_info_duration = QtWidgets.QLabel(self.frame)
        self.label_info_duration.setGeometry(QtCore.QRect(20, 50, 51, 20))
        self.label_info_duration.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_info_duration.setObjectName("label_info_duration")
        self.img_thumbnail_display = QtWidgets.QLabel(self.frame)
        self.img_thumbnail_display.setGeometry(QtCore.QRect(400, 0, 271, 151))
        self.img_thumbnail_display.setText("")
        self.img_thumbnail_display.setPixmap(QtGui.QPixmap("thumb_placeholder.png"))
        self.img_thumbnail_display.setScaledContents(True)
        self.img_thumbnail_display.setObjectName("img_thumbnail_display")
        self.button_thumbnail_download = QtWidgets.QPushButton(self.frame)
        self.button_thumbnail_download.setEnabled(False)
        self.button_thumbnail_download.setGeometry(QtCore.QRect(470, 160, 151, 23))
        self.button_thumbnail_download.setObjectName("button_thumbnail_download")
        self.label_var_name = QtWidgets.QLabel(self.frame)
        self.label_var_name.setGeometry(QtCore.QRect(70, 21, 231, 31))
        self.label_var_name.setText("")
        self.label_var_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_var_name.setIndent(2)
        self.label_var_name.setObjectName("label_var_name")
        self.label_var_duration = QtWidgets.QLabel(self.frame)
        self.label_var_duration.setGeometry(QtCore.QRect(70, 50, 241, 21))
        self.label_var_duration.setText("")
        self.label_var_duration.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_var_duration.setIndent(2)
        self.label_var_duration.setObjectName("label_var_duration")
        self.label_info_description = QtWidgets.QLabel(self.frame)
        self.label_info_description.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.label_info_description.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_info_description.setObjectName("label_info_description")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(60, 80, 341, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setGeometry(QtCore.QRect(20, 0, 311, 101))
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 101))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_var_description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_var_description.setAutoFillBackground(False)
        self.label_var_description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_var_description.setLineWidth(0)
        self.label_var_description.setText("")
        self.label_var_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_var_description.setWordWrap(True)
        self.label_var_description.setIndent(2)
        self.label_var_description.setObjectName("label_var_description")
        self.horizontalLayout.addWidget(self.label_var_description)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_url = QtWidgets.QLabel(self.tab)
        self.label_url.setGeometry(QtCore.QRect(90, 210, 47, 16))
        self.label_url.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.label_url.setObjectName("label_url")
        self.label_folder = QtWidgets.QLabel(self.tab)
        self.label_folder.setGeometry(QtCore.QRect(90, 240, 47, 13))
        self.label_folder.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_folder.setObjectName("label_folder")
        self.label_var_folder = QtWidgets.QLabel(self.tab)
        self.label_var_folder.setGeometry(QtCore.QRect(140, 240, 47, 13))
        self.label_var_folder.setObjectName("label_var_folder")
        self.button_folder_browse = QtWidgets.QPushButton(self.tab)
        self.button_folder_browse.setEnabled(False)
        self.button_folder_browse.setGeometry(QtCore.QRect(470, 240, 75, 23))
        self.button_folder_browse.setObjectName("button_folder_browse")
        self.combo_audio_formats = QtWidgets.QComboBox(self.tab)
        self.combo_audio_formats.setGeometry(QtCore.QRect(550, 210, 71, 22))
        self.combo_audio_formats.setObjectName("combo_audio_formats")
        self.combo_audio_formats.addItem("")
        self.combo_audio_formats.addItem("")
        self.combo_audio_formats.addItem("")
        self.combo_audio_formats.addItem("")
        self.combo_audio_formats.addItem("")
        self.combo_audio_formats.addItem("")
        self.combo_video_formats = QtWidgets.QComboBox(self.tab)
        self.combo_video_formats.setGeometry(QtCore.QRect(550, 210, 71, 22))
        self.combo_video_formats.setIconSize(QtCore.QSize(16, 16))
        self.combo_video_formats.setObjectName("combo_video_formats")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.combo_video_formats.addItem("")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(60, 260, 551, 111))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.check_audioonly = QtWidgets.QCheckBox(self.tab)
        self.check_audioonly.setGeometry(QtCore.QRect(550, 240, 70, 17))
        self.check_audioonly.setObjectName("check_audioonly")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_url_download.setText(_translate("MainWindow", "Download"))
        self.label_videoinfo.setText(_translate("MainWindow", "Video Info:"))
        self.label_info_name.setText(_translate("MainWindow", "Name:"))
        self.label_info_duration.setText(_translate("MainWindow", "Duration:"))
        self.button_thumbnail_download.setText(_translate("MainWindow", "Download Thumbnail"))
        self.label_info_description.setText(_translate("MainWindow", "Description:"))
        self.label_url.setText(_translate("MainWindow", "URL:"))
        self.label_folder.setText(_translate("MainWindow", "Folder:"))
        self.label_var_folder.setText(_translate("MainWindow", "..."))
        self.button_folder_browse.setText(_translate("MainWindow", "Browse"))
        self.combo_audio_formats.setItemText(0, _translate("MainWindow", "mp3"))
        self.combo_audio_formats.setItemText(1, _translate("MainWindow", "wav"))
        self.combo_audio_formats.setItemText(2, _translate("MainWindow", "ogg"))
        self.combo_audio_formats.setItemText(3, _translate("MainWindow", "wma"))
        self.combo_audio_formats.setItemText(4, _translate("MainWindow", "aac"))
        self.combo_audio_formats.setItemText(5, _translate("MainWindow", "flac"))
        self.combo_video_formats.setItemText(0, _translate("MainWindow", "mp4"))
        self.combo_video_formats.setItemText(1, _translate("MainWindow", "mov"))
        self.combo_video_formats.setItemText(2, _translate("MainWindow", "wmv"))
        self.combo_video_formats.setItemText(3, _translate("MainWindow", "avi"))
        self.combo_video_formats.setItemText(4, _translate("MainWindow", "flv"))
        self.combo_video_formats.setItemText(5, _translate("MainWindow", "webm"))
        self.combo_video_formats.setItemText(6, _translate("MainWindow", "mkv"))
        self.check_audioonly.setText(_translate("MainWindow", "Audio Only"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Downloader"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Editor"))
