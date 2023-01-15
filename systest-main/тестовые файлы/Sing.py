# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sing.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QGridLayout, QLabel,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form1(object):
    def setupUi(self, Form1):
        if not Form1.objectName():
            Form1.setObjectName(u"Form1")
        Form1.resize(738, 545)
        Form1.setMinimumSize(QSize(738, 545))
        Form1.setMaximumSize(QSize(738, 545))
        Form1.setStyleSheet(u"QWidget{\n"
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
"	background-color: #f9ed3f;\n"
"}\n"
"\n"
"QTextEdit{\n"
"	padding: 10% 10%;\n"
"	color: #ffc0cb;\n"
"	font-size: 16px;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: #78b0e9;\n"
"	font-style: italic;\n"
"}")
        self.gridLayoutWidget = QWidget(Form1)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(39, 60, 271, 291))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.gridLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMaximumSize(QSize(449, 58))

        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.textEdit_3 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(449, 58))

        self.gridLayout.addWidget(self.textEdit_3, 5, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(449, 23))

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(449, 23))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.textEdit_5 = QTextEdit(self.gridLayoutWidget)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setMaximumSize(QSize(269, 58))

        self.gridLayout.addWidget(self.textEdit_5, 9, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(449, 23))

        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)

        self.label_5 = QLabel(Form1)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 380, 451, 16))
        self.label_5.setStyleSheet(u"color: #fea08e;")
        self.commandLinkButton = QCommandLinkButton(Form1)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(40, 450, 141, 41))
        self.gridLayoutWidget_2 = QWidget(Form1)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(360, 60, 281, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.textEdit_2 = QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(449, 58))

        self.gridLayout_2.addWidget(self.textEdit_2, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(449, 23))

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(449, 23))

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.textEdit_4 = QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        self.textEdit_4.setMaximumSize(QSize(449, 58))

        self.gridLayout_2.addWidget(self.textEdit_4, 3, 0, 1, 1)

        self.label_7 = QLabel(Form1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 30, 651, 16))
        self.label_7.setStyleSheet(u"color: #f9ed3f;\n"
"font-weight:700;\n"
"")
        self.label_8 = QLabel(Form1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(40, 410, 461, 16))

        self.retranslateUi(Form1)

        QMetaObject.connectSlotsByName(Form1)
    # setupUi

    def retranslateUi(self, Form1):
        Form1.setWindowTitle(QCoreApplication.translate("Form1", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form1", u"\u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u043a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u0443\u044e \u043f\u043e\u0447\u0442\u0443 ", None))
        self.label.setText(QCoreApplication.translate("Form1", u"\u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u0444\u0430\u043c\u0438\u043b\u0438\u044e", None))
        self.label_6.setText(QCoreApplication.translate("Form1", u"\u041f\u0440\u0438\u0434\u0443\u043c\u0430\u0439\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_5.setText(QCoreApplication.translate("Form1", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442 \u0430\u0442\u0440\u0435\u0431\u0443\u0435\u0442\u0441\u044f \u0434\u043b\u044f \u0434\u0430\u043b\u044c\u043d\u0435\u0439\u0448\u0435\u0439 \u0440\u0430\u0431\u043e\u0442\u044b \u0441 \u0432\u044b\u043f\u0438\u0441\u043a\u0430\u043c\u0438 ", None))
        self.commandLinkButton.setText(QCoreApplication.translate("Form1", u"\u041f\u0440\u043e\u0434\u043e\u043b\u0436\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Form1", u"\u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u0438\u043c\u044f \u0438 \u043e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_4.setText(QCoreApplication.translate("Form1", u"\u0412\u043f\u0438\u0448\u0438\u0442\u0435 \u0441\u0432\u043e\u044e \u043a\u0430\u0444\u0435\u0434\u0440\u0443 ", None))
        self.label_7.setText(QCoreApplication.translate("Form1", u"\u0414\u043b\u044f \u0440\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u0438 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430 \u0437\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u0435 \u0444\u043e\u0440\u043c\u0443", None))
        self.label_8.setText(QCoreApplication.translate("Form1", u"\u0412\u0430\u0436\u043d\u043e \u0443\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u0432\u043e\u044e \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u0443\u044e \u043a\u043e\u0440\u043f\u043e\u0440\u0430\u0442\u0438\u0432\u043d\u0443\u044e \u043f\u043e\u0447\u0442\u0443", None))
    # retranslateUi

