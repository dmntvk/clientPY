
from PyQt5 import QtCore, QtGui, QtWidgets


class grafikk(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(855, 515)
        Form.setMinimumSize(QtCore.QSize(855, 515))
        Form.setMaximumSize(QtCore.QSize(855, 515))
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(244, 247, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 50, 800, 272))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(800, 272))
        self.tableWidget.setMaximumSize(QtCore.QSize(800, 272))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("selection-background-color: rgb(110, 67, 244);\n"
                                       "\n"
                                       " \n"
                                       "")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(20)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(380, 20, 111, 16))
        self.label.setStyleSheet("background: transparent;")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(650, 15, 154, 32))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton.setFont(font)
        self.pushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border-radius: 10px; \n"
                                      "border-style: outset;\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgb(222, 221, 235);\n"
                                      "color: rgb(113, 75, 244)\n"
                                      "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/next копия.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 15, 191, 32))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px; \n"
                                        "border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(222, 221, 235);\n"
                                        "color: rgb(113, 75, 244)\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/bacc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 410, 113, 21))
        self.lineEdit.setStyleSheet("border-radius: 15px; \n"
                                    "border-style: outset;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 440, 113, 21))
        self.lineEdit_2.setStyleSheet("border-radius: 15px; \n"
                                      "border-style: outset;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 470, 113, 21))
        self.lineEdit_3.setStyleSheet("border-radius: 15px; \n"
                                      "border-style: outset;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(200, 380, 121, 26))
        self.comboBox.setStyleSheet("QComboBox\n"
                                    "{\n"
                                    "border-radius: 10px; \n"
                                    "border-style: outset;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "padding: 1px 0px 1px 25px;\n"
                                    "selection-background-color: rgb(222, 221, 235);\n"
                                    "border: 1px solid #714bf4;\n"
                                    "}\n"
                                    "QComboBox:hover, QPushButton:hover\n"
                                    "{\n"
                                    "background-color: rgb(222, 221, 235);\n"
                                    "color: rgb(113, 75, 244)\n"
                                    "}\n"
                                    "QComboBox:on\n"
                                    "{\n"
                                    "    padding-top: 0px;\n"
                                    "    padding-left: 0px;\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "    selection-background-color: rgb(222, 221, 235);\n"
                                    "}\n"
                                    "\n"
                                    "\n"
                                    "\n"
                                    "QComboBox::drop-down\n"
                                    "{\n"
                                    "     subcontrol-origin: padding;\n"
                                    "     subcontrol-position: top right;\n"
                                    "     width: 15px;\n"
                                    "     color: black;\n"
                                    "     border-left-width: 0px;\n"
                                    "     border-left-color: darkgray;\n"
                                    "     border-left-style: solid; /* just a single line */\n"
                                    "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                    "     border-bottom-right-radius: 3px;\n"
                                    "     padding-left: 10px;\n"
                                    " }\n"
                                    "\n"
                                    "\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(340, 380, 111, 26))
        self.comboBox_2.setStyleSheet("QComboBox\n"
                                      "{\n"
                                      "border-radius: 10px; \n"
                                      "border-style: outset;\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "    padding: 1px 0px 1px 35px;\n"
                                      "selection-background-color: rgb(222, 221, 235);\n"
                                      "border: 1px solid #714bf4;\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox:hover, QPushButton:hover\n"
                                      "{\n"
                                      "background-color: rgb(222, 221, 235);\n"
                                      "color: rgb(113, 75, 244)\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "QComboBox:on\n"
                                      "{\n"
                                      "    padding-top: 0px;\n"
                                      "    padding-left: 0px;\n"
                                      "\n"
                                      "    background-color: rgb(255, 255, 255);\n"
                                      "    selection-background-color: rgb(222, 221, 235);\n"
                                      "}\n"
                                      "\n"
                                      "\n"
                                      "\n"
                                      "QComboBox::drop-down\n"
                                      "{\n"
                                      "     subcontrol-origin: padding;\n"
                                      "     subcontrol-position: top right;\n"
                                      "     width: 15px;\n"
                                      "     color: black;\n"
                                      "     border-left-width: 0px;\n"
                                      "     border-left-color: darkgray;\n"
                                      "     border-left-style: solid; /* just a single line */\n"
                                      "     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
                                      "     border-bottom-right-radius: 3px;\n"
                                      "     padding-left: 10px;\n"
                                      " }\n"
                                      "\n"
                                      "\n"
                                      "")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(230, 410, 33, 16))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(230, 440, 60, 16))
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(230, 470, 52, 16))
        self.label_4.setStyleSheet("background: transparent;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(240, 360, 31, 16))
        self.label_5.setStyleSheet("background: transparent;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(370, 360, 41, 16))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 370, 141, 32))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px; \n"
                                        "border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(222, 221, 235);\n"
                                        "color: rgb(113, 75, 244)\n"
                                        "}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 851, 361))
        self.label_7.setStyleSheet("background: transparent;")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./img/grafbod.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 370, 141, 32))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px; \n"
                                        "border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(222, 221, 235);\n"
                                        "color: rgb(113, 75, 244)\n"
                                        "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/calen копия.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(180, 350, 281, 161))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("./img/sadsad.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(450, 361, 321, 50))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./img/sadsad.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_7.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.comboBox.raise_()
        self.comboBox_2.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "График"))
        self.tableWidget.setSortingEnabled(False)
        self.label.setText(_translate("Form", "График на Июнь"))
        self.pushButton.setText(_translate("Form", "Следующий месяц"))
        self.pushButton_2.setText(_translate("Form", "Вернуться на текущий"))
        self.label_2.setText(_translate("Form", "Имя:"))
        self.label_3.setText(_translate("Form", "Телефон:"))
        self.label_4.setText(_translate("Form", "Услуга:"))
        self.label_5.setText(_translate("Form", "День"))
        self.label_6.setText(_translate("Form", "Время"))
        self.pushButton_3.setText(_translate("Form", "Создать запись"))
        self.pushButton_4.setText(_translate("Form", "Удалить запись"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
