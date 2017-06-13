# -*- coding: utf-8 -*-
"""
Spyder Editor

Author : Harish Ashokkumar

PyQt script for creating a GUI. 
"""

import sys
from PyQt4 import QtGui, QtCore


class HomePage(QtGui.QWidget):
    
    def __init__(self):
        super(HomePage, self).__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        self.setGeometry(600, 600, 250, 150)        
        self.setWindowTitle('Process Manager')    
        
        txt1 = QtGui.QLabel('1. Search by name', self)
        txt1.move(20, 20)
        
        txt2 = QtGui.QLabel('2. Choose from a list' ,self)
        txt2.move(20, 120)
        
        txt3 = QtGui.QLabel('-- OR --',self)
        txt3.move(100, 80)
        
        """
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)
        """
        
        #Search button
        btn = QtGui.QPushButton('Search', self)
        btn.setToolTip('Click to search for specific process')
        btn.resize(btn.sizeHint())
        btn.move(20, 40)
        #This code below is very important for building the entire platform
        btn.clicked.connect(self.showDialog)
        
        #Listing button
        listbtn = QtGui.QPushButton('Listing',self)
        listbtn.setToolTip('Click for list of all processes')
        listbtn.move(20, 140)    # move(col,row)
        #listbtn.clicked.connect(self.)
        
        """
        #Create a text box         
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        """
        
        #Calendar button
        calbtn = QtGui.QPushButton('Calendar',self )
        calbtn.setToolTip('Click to view the calendar')
        calbtn.resize(calbtn.sizeHint())
        
        calbtn.move(20,180)
        calbtn.clicked.connect(self.calendar)
        
        
        
        self.show()
    
    def showDialog(self):
        
        text, ok = QtGui.QInputDialog.getText(self, 'Search box', 
            'Enter the process name:')
        
        if ok:
            self.le.setText(str(text))    #This has to change according to xomplex functions
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        
    
    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def calendar(self): 
        
        
        cal = QtGui.QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QtCore.QDate].connect(self.showDate)
        
        self.lbl = QtGui.QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
        
        self.show()
        
    def showDate(self, date):     
        self.lbl.setText(date.toString())

        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = HomePage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
