# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'finaly.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(900, 600))
        Form.setMaximumSize(QSize(900, 600))
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"")
        self.IMG_1 = QLabel(Form)
        self.IMG_1.setObjectName(u"IMG_1")
        self.IMG_1.setGeometry(QRect(1070, 10, 161, 141))
        self.IMG_1.setPixmap(QPixmap(u"../../Downloads/obj.png"))
        self.IMG_2 = QLabel(Form)
        self.IMG_2.setObjectName(u"IMG_2")
        self.IMG_2.setGeometry(QRect(30, 660, 161, 141))
        self.IMG_2.setPixmap(QPixmap(u"../../Downloads/2obj.png"))
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 20, 901, 31))
        self.INTRO = QHBoxLayout(self.horizontalLayoutWidget)
        self.INTRO.setObjectName(u"INTRO")
        self.INTRO.setContentsMargins(0, 0, 0, 0)
        self.PROGRAMM = QLabel(self.horizontalLayoutWidget)
        self.PROGRAMM.setObjectName(u"PROGRAMM")
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(8)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.PROGRAMM.setFont(font)
        self.PROGRAMM.setStyleSheet(u"font-family: 'Inter';\n"
"font-style: normal;")
        self.PROGRAMM.setAlignment(Qt.AlignCenter)

        self.INTRO.addWidget(self.PROGRAMM)

        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(190, 50, 522, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.creat_nag = QPushButton(self.verticalLayoutWidget)
        self.creat_nag.setObjectName(u"creat_nag")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.creat_nag.sizePolicy().hasHeightForWidth())
        self.creat_nag.setSizePolicy(sizePolicy1)
        self.creat_nag.setMinimumSize(QSize(320, 72))
        self.creat_nag.setMaximumSize(QSize(520, 72))
        self.creat_nag.setCursor(QCursor(Qt.PointingHandCursor))
        self.creat_nag.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.creat_nag)

        self.check_nag = QPushButton(self.verticalLayoutWidget)
        self.check_nag.setObjectName(u"check_nag")
        sizePolicy1.setHeightForWidth(self.check_nag.sizePolicy().hasHeightForWidth())
        self.check_nag.setSizePolicy(sizePolicy1)
        self.check_nag.setMinimumSize(QSize(520, 72))
        self.check_nag.setMaximumSize(QSize(320, 72))
        self.check_nag.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.check_nag)

        self.change_teach = QPushButton(self.verticalLayoutWidget)
        self.change_teach.setObjectName(u"change_teach")
        self.change_teach.setMinimumSize(QSize(520, 72))
        self.change_teach.setMaximumSize(QSize(520, 72))
        self.change_teach.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.change_teach)

        self.helper = QLabel(self.verticalLayoutWidget)
        self.helper.setObjectName(u"helper")
        sizePolicy1.setHeightForWidth(self.helper.sizePolicy().hasHeightForWidth())
        self.helper.setSizePolicy(sizePolicy1)
        self.helper.setMinimumSize(QSize(520, 18))
        self.helper.setMaximumSize(QSize(520, 18))
        self.helper.setCursor(QCursor(Qt.ArrowCursor))
        self.helper.setStyleSheet(u"QLabel{\n"
"color: #4c4c4c;\n"
"font-family: 'Inter';\n"
"font-style: normal;\n"
"}\n"
"")
        self.helper.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.helper)

        self.helper_2 = QPushButton(self.verticalLayoutWidget)
        self.helper_2.setObjectName(u"helper_2")
        self.helper_2.setMinimumSize(QSize(520, 72))
        self.helper_2.setMaximumSize(QSize(520, 72))
        self.helper_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.helper_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.IMG_1.setText("")
        self.IMG_2.setText("")
        self.PROGRAMM.setText(QCoreApplication.translate("Form", u"\u041f\u0420\u041e\u0413\u0420\u0410\u041c\u041c\u0410 \u0414\u041b\u042f \u0424\u041e\u0420\u041c\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u042f \u041d\u0410\u0413\u0420\u0423\u0417\u041a\u0418", None))
        self.creat_nag.setText(QCoreApplication.translate("Form", u"\u0441\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u0443", None))
        self.check_nag.setText(QCoreApplication.translate("Form", u"\u043f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u043e\u0442\u0447\u0435\u0442\u0430", None))
        self.change_teach.setText(QCoreApplication.translate("Form", u"\u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u0440\u0435\u043f\u043e\u0434\u0430\u0432\u0430\u0442\u0435\u043b\u0435\u0439", None))
        self.helper.setText(QCoreApplication.translate("Form", u"\u0427\u0438\u0442\u0430\u0442\u044c \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044e \u043f\u043e \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u043d\u0438\u044e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u043d\u044b\u043c \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0435\u043d\u0438\u0435\u043c", None))
        self.helper_2.setText(QCoreApplication.translate("Form", u"\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
    # retranslateUi

