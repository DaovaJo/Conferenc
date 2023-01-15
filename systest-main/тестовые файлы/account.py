# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(491, 508)
        Form.setStyleSheet(u"QWidget{\n"
"	background: linear-gradient(180deg, #801336 -38.96%, #2D142C 89.51%);\n"
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
"	background-color: #f9ed3f;\n"
"}\n"
"\n"
"QGridLayout{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	font-size:16px;\n"
"	color: #7a7a7a;\n"
"	opacity: 80%;\n"
"	padding: 10% 10%;\n"
"}\n"
"\n"
"QTextEdit:hover{\n"
"	color: #729cfe;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #fea08e;\n"
"}")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(150, 320, 181, 51))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(40, 130, 401, 183))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(399, 61))

        self.gridLayout.addWidget(self.textEdit_2, 1, 0, 1, 1)

        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaximumSize(QSize(399, 61))
        self.textEdit.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(190, 40, 120, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 101, 71))
        self.label.setPixmap(QPixmap(u"\u043e\u0431\u044a\u0435\u043a\u0442\u044b/\u0438\u043a\u043e\u043d\u043a\u0430 \u0430\u043a\u043a.png"))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(38, 110, 401, 20))
        font = QFont()
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #fea08e;\n"
"")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 390, 401, 20))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(60, 420, 361, 24))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"color: #78b0e9;\n"
"font-size: 14px;\n"
"background-color: #121212;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"color: #f9ed3f;\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0435\u0440\u0435\u0434 \u0438\u0441\u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u043e\u0439\u0434\u0438\u0442\u0435", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u0415\u0441\u043b\u0438 \u0432\u044b \u0435\u0449\u0435 \u043d\u0435 \u0437\u0430\u0440\u0435\u0433\u0435\u0441\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u044b \u043f\u0435\u0440\u0435\u0439\u0434\u0438\u0442\u0435 \u043f\u043e \u0441\u0441\u044b\u043b\u043a\u0435 \u043d\u0438\u0436\u0435", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"~ \u0417\u0430\u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c\u0441\u044f ~", None))
    # retranslateUi

