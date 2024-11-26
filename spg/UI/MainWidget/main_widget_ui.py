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
        ReadWidget.resize(612, 767)
        ReadWidget.setStyleSheet(u"QWidget {\n"
"  background-color: #fafafa;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: #2c3e50; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"  font-weight: 400; /*  \u0448\u0440\u0438\u0444\u0442 */\n"
"  margin: 10px;\n"
"}\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a */\n"
"QLabel#heading {\n"
"  color: #34495e; /* \u0422\u0435\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"  font-size: 22px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"  margin-bottom: 15px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u0441\u043d\u0438\u0437\u0443 */\n"
"}\n"
"/* \u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a */\n"
"QLabel#subheading {\n"
"  color: #95a5a6; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"  font-size: 13px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448"
                        "\u0440\u0438\u0444\u0442\u0430 \u0434\u043b\u044f \u043f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"  font-weight: 300;\n"
"  margin-bottom: 12px;\n"
"}\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit {\n"
"  border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"  border: 1px solid #d5dbdb; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"  padding: 10px 20px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043f\u043e\u043b\u044f */\n"
"  background-color: #fff;\n"
"  font-size: 14px;\n"
"  color: #34495e;\n"
"}\n"
"/* \u0421\u0442\u0438\u043b\u044c \u0434\u043b\u044f \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"QLineEdit:focus {\n"
"  border: 1px solid #3498"
                        "db; /* \u0421\u0438\u043d\u044f\u044f \u0440\u0430\u043c\u043a\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"  box-shadow: 0 0 8px rgba(52, 152, 219, 0.4); /*  \u0441\u0432\u0435\u0447\u0435\u043d\u0438\u0435 \u0432\u043e\u043a\u0440\u0443\u0433 \u043f\u043e\u043b\u044f */\n"
"}\n"
"/* \u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u0434\u043b\u044f \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit::placeholder {\n"
"  color: #bdc3c7; /* \u0421\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0446\u0432\u0435\u0442 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 */\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #32746D; /* \u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439 \u0444\u043e\u043d */\n"
"  color: #fff;\n"
"  border-radius: 12px;\n"
"  border: 1px solid #32746D;\n"
"  padding: 12px 25px;  /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
""
                        "  margin-top: 18px;/* \u041e\u0442\u0441\u0442\u0443\u043f \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"  outline: none; /* \u0423\u0431\u0438\u0440\u0430\u0435\u0442 \u043a\u043e\u043d\u0442\u0443\u0440 \u0432\u043e\u043a\u0440\u0443\u0433 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #285D57;\n"
"  border: 1px solid #285D57;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ReadWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainFrame = QFrame(ReadWidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"QFrame {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u043c \u0443\u0433\u043b\u044b */\n"
"    background: #fafafa; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"}")
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
        self.ReadFrame.setStyleSheet(u"QFrame{\n"
"    border: 0px solid #ccc;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u043c \u0443\u0433\u043b\u044b */\n"
"    background: #fafafa; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"}")
        self.ReadFrame.setFrameShape(QFrame.StyledPanel)
        self.ReadFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.ReadFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ReadGB = QGroupBox(self.ReadFrame)
        self.ReadGB.setObjectName(u"ReadGB")
        self.ReadGB.setStyleSheet(u"QGroupBox {\n"
"       background: #f0f0f0; \n"
"       border: 2px solid gray;        /* \u0420\u0430\u043c\u043a\u0430 \u0431\u043b\u043e\u043a\u0430 */\n"
"       border-radius: 8px;           /* \u0421\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 */\n"
"       margin-top: 20 px;             /* \u041e\u0442\u0441\u0442\u0443\u043f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"   }\n"
"\n"
"   QGroupBox::title {\n"
"       subcontrol-origin: margin;    /* \u0420\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u0435 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"       subcontrol-position: top left; /* \u041f\u043e\u0437\u0438\u0446\u0438\u044f \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 (\u0441\u0432\u0435\u0440\u0445\u0443 \u0441\u043b\u0435\u0432\u0430) */\n"
"       padding: 0.5 px;               /* \u041e\u0442\u0441\u0442\u0443\u043f \u0432\u043d\u0443\u0442\u0440\u0438 \u0437"
                        "\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"       color: black;                  /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
"       font: bold 30 px;              /* \u0428\u0440\u0438\u0444\u0442 (\u0436\u0438\u0440\u043d\u044b\u0439, 14px) */\n"
"   }\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.ReadGB)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ReadLW = QListWidget(self.ReadGB)
        self.ReadLW.setObjectName(u"ReadLW")
        self.ReadLW.setStyleSheet(u"QListWidget {\n"
"    border: 1px solid #ccc;\n"
"    border-radius: 10px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u044f\u0435\u043c \u0443\u0433\u043b\u044b */\n"
"    background: #fafafa; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0432\u0438\u0434\u0436\u0435\u0442\u0430 */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px; /* \u041e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432 */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background: #addfad; /* \u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 */\n"
"    color: #000;\n"
"    border-radius: 10px;\n"
"}")

        self.verticalLayout_2.addWidget(self.ReadLW)


        self.verticalLayout_3.addWidget(self.ReadGB)

        self.ChooseBtn = QPushButton(self.ReadFrame)
        self.ChooseBtn.setObjectName(u"ChooseBtn")
        self.ChooseBtn.setStyleSheet(u"QPushButton {\n"
"    margin-top: 7px;  /* \u041f\u043e\u0434\u043d\u044f\u0442\u044c \u043d\u0430 5px \u0432\u0432\u0435\u0440\u0445 */\n"
"}")

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
        self.ReadGB.setTitle(QCoreApplication.translate("ReadWidget", u"\u0421\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u043e\u0432:", None))
        self.ChooseBtn.setText(QCoreApplication.translate("ReadWidget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
    # retranslateUi

