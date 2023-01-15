# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'choose.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(738, 545)
        Form.setMinimumSize(QSize(738, 545))
        Form.setMaximumSize(QSize(738, 545))
        Form.setStyleSheet(u"QWidget{\n"
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
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 210, 401, 51))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(40, 280, 401, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 170, 281, 21))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-50, -10, 841, 41))
        self.widget.setStyleSheet(u"background-color: #78b0e9;")
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-40, 510, 841, 41))
        self.widget_2.setStyleSheet(u"background-color: #78b0e9;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041c\u0430\u0442\u0435\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u0438 \u0435\u0441\u0442\u0432\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u043e \u043d\u0430\u0443\u0447\u043d\u044b\u0435 \u0434\u0438\u0441.", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0430\u0444\u0435\u0434\u0440\u0443 ", None))
    # retranslateUi

