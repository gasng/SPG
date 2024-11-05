# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_widget_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ReadWidget(object):
    def setupUi(self, ReadWidget):
        if not ReadWidget.objectName():
            ReadWidget.setObjectName(u"ReadWidget")
        ReadWidget.resize(612, 733)
        self.verticalLayout = QVBoxLayout(ReadWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainFrame = QFrame(ReadWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.MainFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ReadFrame = QFrame(self.MainFrame)
        self.ReadFrame.setObjectName(u"ReadFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ReadFrame.sizePolicy().hasHeightForWidth())
        self.ReadFrame.setSizePolicy(sizePolicy)
        self.ReadFrame.setMinimumSize(QSize(345, 687))
        self.ReadFrame.setMaximumSize(QSize(345, 16777215))
        self.ReadFrame.setFrameShape(QFrame.StyledPanel)
        self.ReadFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ReadFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ReadGB = QGroupBox(self.ReadFrame)
        self.ReadGB.setObjectName(u"ReadGB")
        self.verticalLayout_2 = QVBoxLayout(self.ReadGB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ReadLW = QListWidget(self.ReadGB)
        self.ReadLW.setObjectName(u"ReadLW")

        self.verticalLayout_2.addWidget(self.ReadLW)


        self.verticalLayout_3.addWidget(self.ReadGB)

        self.ChooseBtn = QPushButton(self.ReadFrame)
        self.ChooseBtn.setObjectName(u"ChooseBtn")

        self.verticalLayout_3.addWidget(self.ChooseBtn)


        self.horizontalLayout.addWidget(self.ReadFrame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.MainFrame)


        self.retranslateUi(ReadWidget)

        QMetaObject.connectSlotsByName(ReadWidget)
    # setupUi

    def retranslateUi(self, ReadWidget):
        ReadWidget.setWindowTitle(QCoreApplication.translate("ReadWidget", u"Form", None))
        self.ReadGB.setTitle(QCoreApplication.translate("ReadWidget", u"\u0427\u0442\u0435\u043d\u0438\u0435", None))
        self.ChooseBtn.setText(QCoreApplication.translate("ReadWidget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
    # retranslateUi

