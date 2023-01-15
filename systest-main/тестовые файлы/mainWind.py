# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWind.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(738, 545)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(738, 545))
        MainWindow.setMaximumSize(QSize(738, 545))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #121212;\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: #78b0e9;\n"
"	border-radius: 20px;\n"
"	font-weight: 700;\n"
"	font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #3c5874;\n"
"}\n"
"\n"
"QGridLayout{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QMenuBar{\n"
"	background-color: #78b0e9;\n"
"	\n"
"	font-size: 12px;\n"
"	font-weight: 700;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #fff;\n"
"}")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        font = QFont()
        font.setPointSize(8)
        self.action.setFont(font)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.action_2.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 200, 401, 51))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 280, 401, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 160, 281, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 738, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu.setGeometry(QRect(361, 265, 190, 118))
        sizePolicy.setHeightForWidth(self.menu.sizePolicy().hasHeightForWidth())
        self.menu.setSizePolicy(sizePolicy)
        self.menu.setBaseSize(QSize(2, 2))
        font1 = QFont()
        font1.setPointSize(12)
        self.menu.setFont(font1)
        icon = QIcon()
        icon.addFile(u"\u043e\u0431\u044a\u0435\u043a\u0442\u044b/\u0438\u043a\u043e\u043d\u043a\u0430 \u0430\u043a\u043a.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u0440\u043e\u0431\u043d\u0435\u0435", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438 \u0435\u0441\u0442\u0432\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u043d\u0430\u0443\u0447\u043d\u044b\u0435 \u0434\u0438\u0441.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0444\u0435\u0434\u0440\u0443 ", None))
        self.menu.setTitle("")
    # retranslateUi

