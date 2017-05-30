import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QApplication, QMessageBox, 
                             QDesktopWidget, QMainWindow, QAction, qApp,QTextEdit,
                             QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon


class HomePage(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        
        self.resize(500,250)
        self.center()

        self.setWindowTitle('CREDO HONOR')    
        self.show()

    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        reply = QMessageBox.question(self, 'Action Needed!',
                                    "Are you sure you want to Quit?", QMessageBox.Yes|
                                    QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = HomePage()
    sys.exit(app.exec_())
