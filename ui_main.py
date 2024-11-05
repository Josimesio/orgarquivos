# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'organizer.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc 
 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(590, 369)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(193, 226, 255, 255), stop:1 rgba(0, 97, 136, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(199, 233, 255, 255), stop:1 rgba(0, 164, 209, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_path = QLineEdit(self.frame_2)
        self.txt_path.setObjectName(u"txt_path")
        self.txt_path.setMinimumSize(QSize(0, 28))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.txt_path.setFont(font)
        self.txt_path.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.txt_path.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_path)

        self.btn_open = QPushButton(self.frame_2)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(120, 28))
        font1 = QFont()
        font1.setPointSize(11)
        self.btn_open.setFont(font1)
        self.btn_open.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	border-top-right-radius:15px; \n"
"	background-color:rgb(255, 255, 255);\n"
"	\n"
"	color: rgb(0, 109, 159);\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{color:#fff;background-color:  rgb(0, 157, 235)}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.btn_organize = QPushButton(self.frame)
        self.btn_organize.setObjectName(u"btn_organize")
        self.btn_organize.setMinimumSize(QSize(200, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.btn_organize.setFont(font2)
        self.btn_organize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_organize.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	color: rgb(0, 109, 159);\n"
"\n"
" }\n"
"\n"
"\n"
"QPushButton:hover{\n"
"	color:#fff;\n"
"	background-color:  rgb(0, 157, 235)\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.btn_organize, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/icon/folder.png\"/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">ORGANIZADOR DE ARQUIVOS</span></p></body></html>", None))
        self.txt_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Selecione a pasta -->", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_organize.setText(QCoreApplication.translate("MainWindow", u"Organize", None))
    # retranslateUi 

