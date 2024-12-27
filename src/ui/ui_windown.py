# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frameTitle = QFrame(self.centralwidget)
        self.frameTitle.setObjectName(u"frameTitle")
        self.frameTitle.setMaximumSize(QSize(16777215, 16777215))
        self.frameTitle.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTitle.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frameTitle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frameTitle)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frameTitle)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frameTitle)

        self.frameData = QFrame(self.centralwidget)
        self.frameData.setObjectName(u"frameData")
        self.frameData.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameData.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frameData)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frameResult = QFrame(self.frameData)
        self.frameResult.setObjectName(u"frameResult")
        self.frameResult.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameResult.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frameResult)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelResult = QLabel(self.frameResult)
        self.labelResult.setObjectName(u"labelResult")
        self.labelResult.setFont(font1)
        self.labelResult.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelResult)


        self.verticalLayout_3.addWidget(self.frameResult)

        self.frameInput = QFrame(self.frameData)
        self.frameInput.setObjectName(u"frameInput")
        self.frameInput.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameInput.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frameInput)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.frameInput)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.day = QLineEdit(self.frameInput)
        self.day.setObjectName(u"day")

        self.horizontalLayout.addWidget(self.day)

        self.label_5 = QLabel(self.frameInput)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.month = QLineEdit(self.frameInput)
        self.month.setObjectName(u"month")

        self.horizontalLayout.addWidget(self.month)

        self.label_6 = QLabel(self.frameInput)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.year = QLineEdit(self.frameInput)
        self.year.setObjectName(u"year")

        self.horizontalLayout.addWidget(self.year)

        self.btnCalc = QPushButton(self.frameInput)
        self.btnCalc.setObjectName(u"btnCalc")

        self.horizontalLayout.addWidget(self.btnCalc)


        self.verticalLayout_3.addWidget(self.frameInput)


        self.verticalLayout.addWidget(self.frameData)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contador de Idade", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Preencha sua data de nascimento", None))
        self.labelResult.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DIA", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"M\u00caS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ANO", None))
        self.btnCalc.setText(QCoreApplication.translate("MainWindow", u"CALCULAR", None))
    # retranslateUi

