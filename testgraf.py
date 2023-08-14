
from PyQt5 import QtCore, QtGui, QtWidgets


class graffik(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(794, 598)
        Form.setMinimumSize(QtCore.QSize(794, 598))
        Form.setMaximumSize(QtCore.QSize(794, 598))
        Form.setStyleSheet("")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(-120, 4, 921, 301))
        self.calendarWidget.setStyleSheet("#qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"\n"
"#qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/*  год, месяц                                                */\n"
"#qt_calendar_yearbutton, #qt_calendar_monthbutton {\n"
"    color: white;\n"
"    margin: 18px;\n"
"    min-width: 60px;\n"
"    border-radius: 30px;\n"
"}\n"
"#qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {\n"
"    background-color: rgba(225, 225, 225, 100);\n"
"}\n"
"#qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Поле ввода года                                                        */\n"
"#qt_calendar_yearedit {\n"
"    min-width: 50px;\n"
"    color: white;\n"
"    background: transparent;         /* Сделать фон окна ввода прозрачным */\n"
"}\n"
"#qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */\n"
"    width: 20px;\n"
"    subcontrol-position: right;      \n"
"}\n"
"#qt_calendar_yearedit::down-button { /* Кнопка вниз     */\n"
"    width: 20px;\n"
"    subcontrol-position: left;       \n"
"}\n"
"\n"
"/* меню выбора месяца                                          */\n"
"CalendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"}\n"
"CalendarWidget QToolButton QMenu::item {\n"
"    padding: 10px;\n"
"}\n"
"CalendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"CalendarWidget QToolButton::menu-indicator {\n"
"/*  image: none;        Удалите маленькую стрелку под выбором месяца !!! */\n"
"    subcontrol-position: right center;                /* Право по центру */\n"
"}\n"
"\n"
"/* ниже календарной формы */\n"
"#qt_calendar_calendarview {\n"
"    outline: 10px; \n"
"    selection-background-color: rgb(0, 188, 212);\n"
"}\n"
"")
        self.calendarWidget.setObjectName("calendarWidget")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(37, 326, 719, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setStyleSheet("selection-background-color: rgb(0, 188, 212);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-60, -20, 871, 641))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./img/fon.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 801, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./img/ggpp.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 10, 30, 30))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"border-radius: 10px; \n"
"border-style: outset;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(222, 221, 235);\n"
"color: rgb(113, 75, 244)\n"
"}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/bacc1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(740, 10, 30, 30))
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
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/next1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(28, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 26, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(-130, 60, 931, 41))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("./img/ggpp.png"))
        self.label_5.setScaledContents(False)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(44, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(159, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(272, 70, 21, 17))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(387, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(503, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(617, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(733, 70, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(-20, 300, 821, 301))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("./img/fonnn.png"))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(10, 300, 771, 291))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("./img/block.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(390, 521, 321, 50))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("./img/1SDW.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 530, 141, 32))
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
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(560, 530, 141, 32))
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
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 470, 113, 21))
        self.lineEdit.setStyleSheet("border-radius: 15px; \n"
"border-style: outset;\n"
"background-color: rgb(222, 221, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(60, 530, 52, 16))
        self.label_16.setStyleSheet("background: transparent;")
        self.label_16.setObjectName("label_16")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 530, 113, 21))
        self.lineEdit_3.setStyleSheet("border-radius: 15px; \n"
"border-style: outset;\n"
"background-color: rgb(222, 221, 235);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(300, 450, 41, 16))
        self.label_17.setStyleSheet("background: transparent;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(30, 450, 221, 121))
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("./img/sadsad.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(270, 470, 111, 26))
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
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(60, 500, 60, 16))
        self.label_19.setStyleSheet("background: transparent;")
        self.label_19.setObjectName("label_19")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 500, 113, 21))
        self.lineEdit_2.setStyleSheet("border-radius: 15px; \n"
"border-style: outset;\n"
"background-color: rgb(222, 221, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(60, 470, 33, 16))
        self.label_20.setStyleSheet("background: transparent;")
        self.label_20.setObjectName("label_20")
        self.label.raise_()
        self.label_13.raise_()
        self.calendarWidget.raise_()
        self.label_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_14.raise_()
        self.tableWidget.raise_()
        self.label_15.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_18.raise_()
        self.comboBox_2.raise_()
        self.label_19.raise_()
        self.lineEdit_2.raise_()
        self.label_20.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.lineEdit.raise_()
        self.lineEdit_3.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton_3.clicked.connect(self.sels)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Сентябрь"))
        self.label_4.setText(_translate("Form", "2022"))
        self.label_6.setText(_translate("Form", "Пн"))
        self.label_7.setText(_translate("Form", "Вт"))
        self.label_8.setText(_translate("Form", "Ср"))
        self.label_9.setText(_translate("Form", "Чт"))
        self.label_10.setText(_translate("Form", "Пт"))
        self.label_11.setText(_translate("Form", "Сб"))
        self.label_12.setText(_translate("Form", "Вс"))
        self.pushButton_3.setText(_translate("Form", "Создать запись"))
        self.pushButton_4.setText(_translate("Form", "Удалить запись"))
        self.label_16.setText(_translate("Form", "Услуга:"))
        self.label_17.setText(_translate("Form", "Время"))
        self.label_19.setText(_translate("Form", "Телефон:"))
        self.label_20.setText(_translate("Form", "Имя:"))

    def sels(self):
        aboba = self.calendarWidget.selectedDate().month()
        print(aboba)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = graffik()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())