# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import (QLabel, QPlainTextEdit,
    QPushButton, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(763, 343)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LoadMP3 = QPushButton(self.centralwidget)
        self.LoadMP3.setObjectName(u"LoadMP3")
        self.LoadMP3.setGeometry(QRect(11, 20, 181, 61))
        font = QFont()
        font.setFamilies([u"Weibei SC"])
        font.setPointSize(24)
        font.setBold(True)
        self.LoadMP3.setFont(font)
        self.SongName = QPlainTextEdit(self.centralwidget)
        self.SongName.setObjectName(u"SongName")
        self.SongName.setGeometry(QRect(121, 90, 301, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(11, 90, 141, 31))
        self.label.setFont(font)
        self.SingerName = QPlainTextEdit(self.centralwidget)
        self.SingerName.setObjectName(u"SingerName")
        self.SingerName.setGeometry(QRect(121, 130, 301, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 130, 141, 31))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(11, 170, 141, 31))
        self.label_3.setFont(font)
        self.AlbumName = QPlainTextEdit(self.centralwidget)
        self.AlbumName.setObjectName(u"AlbumName")
        self.AlbumName.setGeometry(QRect(121, 170, 301, 31))
        self.Start = QPushButton(self.centralwidget)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(11, 220, 411, 71))
        self.Start.setFont(font)
        self.LoadJPG = QPushButton(self.centralwidget)
        self.LoadJPG.setObjectName(u"LoadJPG")
        self.LoadJPG.setGeometry(QRect(201, 20, 221, 61))
        self.LoadJPG.setFont(font)
        self.image = QLabel(self.centralwidget)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(440, 20, 300, 300))
        self.image.setPixmap(QPixmap(u"../Yulan.jpg"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"歌曲信息填写", None))
        self.LoadMP3.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7dMP3\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u66f2\u540d\u79f0:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6b4c\u624b\u540d\u79f0:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4e13\u8f91\u540d\u79f0:", None))
        self.Start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8f6c\u6362", None))
        self.LoadJPG.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7dJPEG\u683c\u5f0f\u56fe\u7247", None))
        self.image.setText("")
    # retranslateUi

