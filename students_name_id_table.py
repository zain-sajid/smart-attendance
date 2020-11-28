# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtWidgets, QtGui, QtCore
import mysql.connector

class Ui_MainWindow(object):
    def loadData(self):
        connection = mysql.connector.connect(host='localhost', database='Attendance_Management_System', user='root', passwd='Password@123')
        sql_select_Query = 'SELECT * from hu100'
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print('total number of rows in cs114 is: ',cursor.rowcount)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        end = cursor.rowcount
        for i in range(cursor.rowcount):
            self.tableWidget.insertRow(i)
        print('\nPrinting each record')
        counter = 0
        print(records)
        for row in records:
            self.tableWidget.setItem(counter,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(counter,1,QtWidgets.QTableWidgetItem(str(row[1])))
            print("name = ",row[0])
            print("id = ",row[1], '\n')
            counter += 1


        connection.close()
        cursor.close()
        print('MYSQL connection closed')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setGeometry(QtCore.QRect(310, 410, 56, 17))
        self.btn_load.setObjectName("btn_load")

        self.btn_load.clicked.connect(self.loadData)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(6, 6, 681, 401))
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(14)
        self.tableWidget.setObjectName("tableWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Smart Attendance"))
        self.btn_load.setText(_translate("MainWindow", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

