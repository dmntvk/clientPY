from PyQt5 import QtCore, QtGui, QtWidgets


class editor(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(679, 427)
        Form.setMinimumSize(QtCore.QSize(679, 427))
        Form.setMaximumSize(QtCore.QSize(679, 427))
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(244, 247, 255, 255), stop:1 rgba(255, 255, 255, 255))")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(57, 20, 91, 16))
        self.label.setStyleSheet("background: transparent;")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 53, 231, 291))
        self.listWidget.setStyleSheet("border-radius: 15px; \n"
                                      "border-style: outset;")
        self.listWidget.setObjectName("listWidget")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(153, 377, 113, 32))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px; \n"
                                        "border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(222, 221, 235);\n"
                                        "color: rgb(113, 75, 244)\n"
                                        "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/calen копия.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setCheckable(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(21, 377, 131, 32))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "border-radius: 10px; \n"
                                        "border-style: outset;\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "background-color: rgb(222, 221, 235);\n"
                                        "color: rgb(113, 75, 244)\n"
                                        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/sts.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 65, 37, 16))
        self.label_2.setStyleSheet("background: transparent;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(340, 63, 113, 21))
        self.lineEdit.setStyleSheet("border-radius: 15px; \n"
                                    "border-style: outset;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(470, 65, 47, 16))
        self.label_3.setStyleSheet("background: transparent;")
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 63, 113, 21))
        self.lineEdit_2.setStyleSheet("border-radius: 15px; \n"
                                      "border-style: outset;\n"
                                      "background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(310, 123, 91, 16))
        self.label_4.setStyleSheet("background: transparent;")
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(300, 143, 353, 201))
        self.textEdit.setStyleSheet("border-radius: 15px; \n"
                                
                                "border-style: outset;")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(428, 377, 102, 32))
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 3, 271, 361))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./img/editbdbodu.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 13, 25, 30))
        self.label_6.setStyleSheet("background: transparent;")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("./img/uod.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 369, 271, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./img/cnopki.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(280, 3, 391, 361))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("./img/editbdbodu.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(302, 53, 341, 41))
        self.widget.setStyleSheet("border-radius: 15px; \n"
                                  "border-style: outset;")
        self.widget.setObjectName("widget")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(290, 369, 381, 51))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./img/cnopki.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(303, 13, 25, 30))
        self.label_10.setStyleSheet("background: transparent;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("./img/uod.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(330, 20, 91, 16))
        self.label_11.setStyleSheet("background: transparent;")
        self.label_11.setObjectName("label_11")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(428, 377, 106, 32))
        self.pushButton1.setStyleSheet("QPushButton{\n"
                                       "border-radius: 10px; \n"
                                       "border-style: outset;\n"
                                       "background-color: rgb(255, 255, 255);\n"
                                       "}\n"
                                       "QPushButton:hover{\n"
                                       "background-color: rgb(222, 221, 235);\n"
                                       "color: rgb(113, 75, 244)\n"
                                       "}")
        self.pushButton1.setIcon(icon2)
        self.pushButton1.setIconSize(QtCore.QSize(30, 30))
        self.pushButton1.setObjectName("pushButton1")
        self.label_9.raise_()
        self.label_8.raise_()
        self.widget.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label.raise_()
        self.listWidget.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.label_3.raise_()
        self.lineEdit_2.raise_()
        self.label_4.raise_()
        self.textEdit.raise_()
        self.pushButton.raise_()
        self.label_6.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton1.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Работа с базой клиентов"))
        self.label.setText(_translate("Form", "База клиентов"))
        self.pushButton_2.setText(_translate("Form", "Удалить"))
        self.pushButton_3.setText(_translate("Form", "Редактировать"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Номер"))
        self.label_4.setText(_translate("Form", "Особенности"))
        self.pushButton.setText(_translate("Form", "Добавить"))
        self.label_11.setText(_translate("Form", "Анкета"))
        self.pushButton1.setText(_translate("Form", "Изменить"))
        self.pushButton1.hide()


