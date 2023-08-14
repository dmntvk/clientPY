# from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from clientPY import Ui_MainWindow
from editorbd import editor
from grafik import grafikk
from datetime import datetime
import sys
import sqlite3
from testgraf import graffik

dt = datetime.today()
day = dt.day
timer = QtCore.QTimer()

def mount1():
    global mes
    if dt.month == 1:
        mes = " Января"
    elif dt.month == 2:
        mes = " Февраля"
    elif dt.month == 3:
        mes = " Марта"
    elif dt.month == 4:
        mes = " Апреля"
    elif dt.month == 5:
        mes = " Мая"
    elif dt.month == 6:
        mes = " Июня"
    elif dt.month == 7:
        mes = " Июля"
    elif dt.month == 8:
        mes = " Августа"
    elif dt.month == 9:
        mes = " Сентября"
    elif dt.month == 10:
        mes = " Октября"
    elif dt.month == 11:
        mes = " Ноября"
    elif dt.month == 12:
        mes = " Декабря"

    return mes
mount1()
dm = str(dt.month)
dy = str(dt.year)

day_m = str(day) + "." + "0"+ dm + "." +dy
print(day_m)






app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
client = Ui_MainWindow()
client.setupUi(MainWindow)
MainWindow.show()


def openEditor():
    global Form
    Form = QtWidgets.QWidget()
    edi = editor()
    edi.setupUi(Form)
    Form.show()
    connection = sqlite3.connect('client.sqlite')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM client')
    users = cursor.fetchall()
    for user in users:
        edi.listWidget.addItem(f'{user[1]} | {user[3]}')
    cursor.close()
    connection.close()
    def update():
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        name = edi.lineEdit.text()
        phone = edi.lineEdit_2.text()
        osobi = edi.textEdit.toPlainText()
        cursor.execute('INSERT INTO client (name, osobinosti, phone) VALUES (\'%s\', \'%s\', \'%s\')'%(name, osobi, phone))
        connection.commit()
        edi.listWidget.clear()
        cursor.execute('SELECT * FROM client')
        users = cursor.fetchall()
        for user in users:
            edi.listWidget.addItem(f'{user[1]} | {user[3]}')
        cursor.close()
        connection.close()
        _translate = QtCore.QCoreApplication.translate
        edi.lineEdit.setText(_translate("Form", ""))
        edi.lineEdit_2.setText(_translate("Form", ""))
        edi.textEdit.setText(_translate("Form", ""))
    edi.pushButton.clicked.connect(update)
    def edites():
        global idd
        edi.listWidget.currentItem().text()
        _translate = QtCore.QCoreApplication.translate
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM client')
        users = cursor.fetchall()
        for user in users:
           if f'{user[1]} | {user[3]}' == edi.listWidget.currentItem().text():
               edi.lineEdit.setText(_translate("Form", f'{user[1]}'))
               edi.lineEdit_2.setText(_translate("Form", f'{user[3]}'))
               edi.textEdit.setText(_translate("Form", f'{user[2]}'))
               idd = f'{user[0]}'
        cursor.close()
        connection.close()
        edi.pushButton.hide()
        edi.pushButton1.show()
        return idd
    edi.listWidget.itemActivated.connect(edites)
    edi.pushButton_3.clicked.connect(edites)
    def editess():
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM client')
        users = cursor.fetchall()
        for user in users:
            if idd == f'{user[0]}':
                name = edi.lineEdit.text()
                osobi = edi.textEdit.toPlainText()
                phone = edi.lineEdit_2.text()
                cursor.execute('UPDATE client SET name = ? WHERE id = ? ', (name, idd))
                cursor.execute('UPDATE client SET osobinosti = ? WHERE id = ? ', (osobi, idd))
                cursor.execute('UPDATE client SET phone = ? WHERE id = ? ', (phone, idd))
        connection.commit()
        edi.listWidget.clear()
        cursor.execute('SELECT * FROM client')
        users = cursor.fetchall()
        for user in users:
            edi.listWidget.addItem(f'{user[1]} | {user[3]}')
        cursor.close()
        connection.close()
        edi.pushButton1.hide()
        edi.pushButton.show()
        _translate = QtCore.QCoreApplication.translate
        edi.lineEdit.setText(_translate("Form", ""))
        edi.lineEdit_2.setText(_translate("Form", ""))
        edi.textEdit.setText(_translate("Form", ""))
    edi.pushButton1.clicked.connect(editess)
    def delli():
        global fofs
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM client')
        users = cursor.fetchall()
        for user in users:
            if f'{user[1]} | {user[3]}' == edi.listWidget.currentItem().text():
                fofs = f'{user[0]}'
        cursor.close()
        connection.close()
        return fofs
    edi.listWidget.itemSelectionChanged.connect(delli)

    def showDialog():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f'Вы точно хотите удалить клиента:\n {edi.listWidget.currentItem().text()}')
        msgBox.setWindowTitle("Удаление клиента")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)


        def dellii():
            connection = sqlite3.connect('client.sqlite')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM client')
            users = cursor.fetchall()
            for user in users:
                if fofs == f'{user[0]}':
                    cursor.execute('DELETE from client where id = ?', (fofs, ))
            connection.commit()
            edi.listWidget.clear()
            cursor.execute('SELECT * FROM client')
            users = cursor.fetchall()
            for user in users:
                edi.listWidget.addItem(f'{user[1]} | {user[3]}')
            cursor.close()
            connection.close()
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            dellii()
        elif returnValue == QMessageBox.No:
            msgBox.close()
    edi.pushButton_2.clicked.connect(showDialog)

def testFraf():
    global Form1
    Form1 = QtWidgets.QWidget()
    ui = graffik()
    ui.setupUi(Form1)
    Form1.show()
    global mouns1, gg
    gg = ui.calendarWidget.selectedDate().year()
    mouns1 = ui.calendarWidget.selectedDate().month()


    def mount():
        mouns = ui.calendarWidget.selectedDate().month()
        mouns1 = mouns
        if mouns == 1:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Январь"))
        elif mouns == 2:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Февраль"))
        elif mouns == 3:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Март"))
        elif mouns == 4:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Апрель"))
        elif mouns == 5:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Май"))
        elif mouns == 6:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июнь"))
        elif mouns == 7:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июль"))
        elif mouns == 8:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Август"))
        elif mouns == 9:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Сентябрь"))
        elif mouns == 10:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Октябрь"))
        elif mouns == 11:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Ноябрь"))
        elif mouns == 12:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Декабрь"))
        print(mouns1)
        return mouns1


    mount()

    def timegen():
        global ti
        ti = []
        for x in range(10, 22):
            pop = x
            for y in range(00, 4, 3):
                tim = f'{pop}:{y}0'
                ti.append(tim)
        ui.tableWidget.setRowCount(len(ti))
        ui.tableWidget.setVerticalHeaderLabels(ti)
        for y in range(0, len(ti)+1):
            ui.tableWidget.showRow(y)
        return ti
    timegen()
    def datgen():
        dat = str(ui.calendarWidget.selectedDate().day())
        datt = ui.calendarWidget.selectedDate().month()
        if datt == 1:
            datt = " Январь"
        elif datt == 2:
            datt = " Февраля"
        elif datt == 3:
            datt = " Марта"
        elif datt == 4:
            datt = " Апреля"
        elif datt == 5:
            datt = " Мая"
        elif datt == 6:
            datt = " Июня"
        elif datt == 7:
            datt = " Июля"
        elif datt == 8:
            datt = " Августа"
        elif datt == 9:
            datt = " Сентября"
        elif datt == 10:
            datt = " Октября"
        elif datt == 11:
            datt = " Ноября"
        elif datt == 12:
            datt = " Декабря"
        goog = dat + datt
        lis = [goog]
        ui.tableWidget.setColumnCount(1)
        ui.tableWidget.setHorizontalHeaderLabels(lis)
        header = ui.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
    datgen()



    def newmount():
        _translate = QtCore.QCoreApplication.translate
        global mouns1, gg
        if mouns1 == 12:
            mouns1 = 0
            gg = gg +1
            ui.label_4.setText(_translate("Form", str(gg)))
        mouns1 = mouns1 + 1
        if mouns1 == 1:
            ui.label_3.setText(_translate("Form", "Январь"))
        elif mouns1 == 2:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Февраль"))
        elif mouns1 == 3:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Март"))
        elif mouns1 == 4:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Апрель"))
        elif mouns1 == 5:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Май"))
        elif mouns1 == 6:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июнь"))
        elif mouns1 == 7:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июль"))
        elif mouns1 == 8:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Август"))
        elif mouns1 == 9:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Сентябрь"))
        elif mouns1 == 10:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Октябрь"))
        elif mouns1 == 11:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Ноябрь"))
        elif mouns1 == 12:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Декабрь"))
        return mouns1, gg
    def nexmount():
        ui.calendarWidget.showNextMonth()
        newmount()
        return mount1, gg
    ui.pushButton.clicked.connect(nexmount)
    def backmount1():
        _translate = QtCore.QCoreApplication.translate
        global mouns1, gg
        if mouns1 == 1:
            mouns1 = 13
            gg = gg - 1
            ui.label_4.setText(_translate("Form", str(gg)))
        mouns1 = mouns1 - 1
        if mouns1 == 1:
            ui.label_3.setText(_translate("Form", "Январь"))
        elif mouns1 == 2:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Февраль"))
        elif mouns1 == 3:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Март"))
        elif mouns1 == 4:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Апрель"))
        elif mouns1 == 5:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Май"))
        elif mouns1 == 6:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июнь"))
        elif mouns1 == 7:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Июль"))
        elif mouns1 == 8:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Август"))
        elif mouns1 == 9:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Сентябрь"))
        elif mouns1 == 10:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Октябрь"))
        elif mouns1 == 11:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Ноябрь"))
        elif mouns1 == 12:
            _translate = QtCore.QCoreApplication.translate
            ui.label_3.setText(_translate("Form", "Декабрь"))
        return mouns1, gg
    def backmount():
        ui.calendarWidget.showPreviousMonth()
        backmount1()
        return mouns1, gg
        newmount()
    ui.pushButton_2.clicked.connect(backmount)
    def loadbd():
        ui.tableWidget.clear()
        datgen()
        timegen()
        dd = str(ui.calendarWidget.selectedDate().day())
        mm = str(ui.calendarWidget.selectedDate().month())
        yy = str(ui.calendarWidget.selectedDate().year())
        mdy = dd +".0" + mm + "." + yy
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM grafik')
        users = cursor.fetchall()
        _translate = QtCore.QCoreApplication.translate
        __sortingEnabled = ui.tableWidget.isSortingEnabled()
        ui.tableWidget.setSortingEnabled(False)
        for user in users:
            a = 0
            if str(mdy) == user[5]:
                try:
                    while a <= 4:
                        item = QtWidgets.QTableWidgetItem()
                        ui.tableWidget.setItem(int(user[1]) + a, 0, item)
                        item = ui.tableWidget.item(int(user[1]) + a, 0)
                        item.setText(_translate("Form", f'{user[3]} | {user[4]} | {user[2]}'))
                        a += 1
                        if str(mdy) == user[5]:
                            for b in range(int(user[1]), int(user[1]) + 4):
                                ui.tableWidget.hideRow(b + 1)
                except AttributeError:
                    while a < 1:
                        item = QtWidgets.QTableWidgetItem()
                        ui.tableWidget.setItem(int(user[1]) + a, 0, item)
                        item = ui.tableWidget.item(int(user[1]) + a, 0)
                        item.setText(_translate("Form", f'{user[3]} | {user[4]} | {user[2]}'))
                        a += 1

        cursor.close()
        connection.close()
        ui.tableWidget.setSortingEnabled(__sortingEnabled)
    loadbd()
    def loadcomb():
        ui.comboBox_2.clear()
        for x in range(0, 24):
            if ui.tableWidget.item(x, 0) == None:
                ui.comboBox_2.addItem(ti[x])
            else:
                pass
    loadcomb()
    def pl():
        mount()
        datgen()
        loadbd()
        loadcomb()
    ui.calendarWidget.clicked.connect(pl)

    def new_client():
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        name = ui.lineEdit.text()
        phone = ui.lineEdit_2.text()
        usluga = ui.lineEdit_3.text()
        def uicombo():
            global asd
            global ttt
            if ui.comboBox_2.currentText() == "10:00":
                asd = 0
                ttt = "10:00"
            elif ui.comboBox_2.currentText() == "10:30":
                asd = 1
                ttt = "10:30"
            elif ui.comboBox_2.currentText() == "11:00":
                asd = 2
                ttt = "11:00"
            elif ui.comboBox_2.currentText() == "11:30":
                asd = 3
                ttt = "11:30"
            elif ui.comboBox_2.currentText() == "12:00":
                asd = 4
                ttt = "12:00"
            elif ui.comboBox_2.currentText() == "12:30":
                asd = 5
                ttt = "12:30"
            elif ui.comboBox_2.currentText() == "13:00":
                asd = 6
                ttt = "13:00"
            elif ui.comboBox_2.currentText() == "13:30":
                asd = 7
                ttt = "13:30"
            elif ui.comboBox_2.currentText() == "14:00":
                asd = 8
                ttt = "14:00"
            elif ui.comboBox_2.currentText() == "14:30":
                asd = 9
                ttt = "14:30"
            elif ui.comboBox_2.currentText() == "15:00":
                asd = 10
                ttt = "15:00"
            elif ui.comboBox_2.currentText() == "15:30":
                asd = 11
                ttt = "15:30"
            elif ui.comboBox_2.currentText() == "16:00":
                asd = 12
                ttt = "16:00"
            elif ui.comboBox_2.currentText() == "16:30":
                asd = 13
                ttt = "16:30"
            elif ui.comboBox_2.currentText() == "17:00":
                asd = 14
                ttt = "17:00"
            elif ui.comboBox_2.currentText() == "17:30":
                asd = 15
                ttt = "17:30"
            elif ui.comboBox_2.currentText() == "18:00":
                asd = 16
                ttt = "18:00"
            elif ui.comboBox_2.currentText() == "18:30":
                asd = 17
                ttt = "18:30"
            elif ui.comboBox_2.currentText() == "19:00":
                asd = 18
                ttt = "19:00"
            elif ui.comboBox_2.currentText() == "19:30":
                asd = 19
                ttt = "19:30"
            elif ui.comboBox_2.currentText() == "20:00":
                asd = 20
                ttt = "20:00"
            elif ui.comboBox_2.currentText() == "20:30":
                asd = 21
                ttt = "20:30"
            elif ui.comboBox_2.currentText() == "21:00":
                asd = 22
                ttt = "21:00"
            elif ui.comboBox_2.currentText() == "21:30":
                asd = 23
                ttt = "21:30"
            return asd, ttt
        uicombo()
        dd = str(ui.calendarWidget.selectedDate().day())
        mm = str(ui.calendarWidget.selectedDate().month())
        yy = str(ui.calendarWidget.selectedDate().year())
        mdy = dd +".0" + mm + "." + yy
        time = asd
        time_zap = ttt
        moun = mdy
        cursor.execute(
            'INSERT INTO grafik (time, yslyga, name, phone, mount, time_zap) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' % (
            time, usluga, name, phone, moun, time_zap))
        connection.commit()
        cursor.close()
        connection.close()
        loadbd()
        ui.lineEdit.clear()
        ui.lineEdit_2.clear()
        ui.lineEdit_3.clear()
        loadcomb()
    ui.pushButton_3.clicked.connect(new_client)

    def dellzap():
        global fofss
        connection = sqlite3.connect('client.sqlite')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM grafik')
        users = cursor.fetchall()
        for user in users:
            try:
                if f'{user[3]} | {user[4]} | {user[2]}' == ui.tableWidget.currentItem().text():
                    fofss = f'{user[0]}'
            except AttributeError:
                return
        cursor.close()
        connection.close()
        try:
            return fofss
        except NameError:
            return
    ui.tableWidget.itemSelectionChanged.connect(dellzap)

    def showDialog1():
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(f'Вы точно хотите удалить запись клиента клиента:\n {ui.tableWidget.currentItem().text()}')
        msgBox.setWindowTitle("Удаление записи клиента")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        def dellii1():
            connection = sqlite3.connect('client.sqlite')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM grafik')
            users = cursor.fetchall()
            for user in users:
                if fofss == f'{user[0]}':
                    cursor.execute('DELETE from grafik where id = ?', (fofss,))
            connection.commit()
            ui.tableWidget.clear()
            cursor.execute('SELECT * FROM grafik')
            users = cursor.fetchall()
            _translate = QtCore.QCoreApplication.translate
            datgen()
            timegen()
            dd = str(ui.calendarWidget.selectedDate().day())
            mm = str(ui.calendarWidget.selectedDate().month())
            yy = str(ui.calendarWidget.selectedDate().year())
            mdy = dd + ".0" + mm + "." + yy
            for user in users:
                a = 0
                if str(mdy) == user[5]:
                    try:
                        while a <= 4:
                            item = QtWidgets.QTableWidgetItem()
                            ui.tableWidget.setItem(int(user[1]) + a, 0, item)
                            item = ui.tableWidget.item(int(user[1]) + a, 0)
                            item.setText(_translate("Form", f'{user[3]} | {user[4]} | {user[2]}'))
                            a += 1
                            if str(mdy) == user[5]:
                                for b in range(int(user[1]), int(user[1]) + 4):
                                    ui.tableWidget.hideRow(b + 1)
                    except AttributeError:
                        while a < 1:
                            item = QtWidgets.QTableWidgetItem()
                            ui.tableWidget.setItem(int(user[1]) + a, 0, item)
                            item = ui.tableWidget.item(int(user[1]) + a, 0)
                            item.setText(_translate("Form", f'{user[3]} | {user[4]} | {user[2]}'))
                            a += 1
            cursor.close()
            connection.close()

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Yes:
            dellii1()
            loadcomb()
        elif returnValue == QMessageBox.No:
            msgBox.close()
    ui.pushButton_4.clicked.connect(showDialog1)

def tydaylist():
    client.listWidget.clear()
    connection = sqlite3.connect('client.sqlite')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM grafik')
    users = cursor.fetchall()
    client.listWidget.setSortingEnabled(False)
    for user in users:
        if f'{user[5]}' == day_m:
            client.listWidget.addItem(f'{user[6]} | {user[3]} | {user[4]}')

    cursor.close()
    connection.close()
tydaylist()

def listwiye():
    client.client_txt1.clear()
    client.time_txt.clear()
    client.phone_txt2.clear()
    client.yslyga_txt2.clear()
    _translate = QtCore.QCoreApplication.translate
    connection = sqlite3.connect('client.sqlite')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM grafik')
    users = cursor.fetchall()
    for user in users:
        if f'{user[6]} | {user[3]} | {user[4]}' == client.listWidget.currentItem().text():
            client.client_txt1.setText(f'{user[3]}')
            client.time_txt.setText(f'{user[6]}')
            client.phone_txt2.setText(f'{user[4]}')
            client.yslyga_txt2.setText(f'{user[2]}')
            client.textBrowser.setHtml(_translate("MainWindow", "Клиент еще не добавлен в базу постоянных клиентов"))
            if f'{user[6]} | {user[3]} | {user[4]}' == client.listWidget.currentItem().text():
                _translate = QtCore.QCoreApplication.translate
                cursor.execute('SELECT * FROM client')
                users1 = cursor.fetchall()
                for user1 in users1:
                        if f'{user1[3]}' == f'{user[4]}':
                            try:
                                client.textBrowser.setHtml(_translate("MainWindow", f'{user1[2]}'))
                            except IndexError:
                                return




    cursor.close()
    connection.close()
client.listWidget.itemActivated.connect(listwiye)


def updatebd():
    tydaylist()

client.updbtn.clicked.connect(updatebd)
client.grafikb.clicked.connect(testFraf)
client.pushButton.clicked.connect(openEditor)

sys.exit(app.exec_())
