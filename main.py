"""
    Author: Sabar Singh Ahuja
"""
import sys
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

## FOR 4K DISPLAYS
if hasattr( Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

if hasattr( Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

"""
Main object which manages UI anf functionalities for all 4 pages
"""
class MainWindow(QMainWindow):
    #default constructor for main window declaring objects for different pages and variables to store data to retain data between switching pages
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowFlags(Qt.Window )

        self.mergeTab = MergePdfWindow()
        self.updateTab = UpdatePdfWindow()
        self.deleteTab = DeletePageWindow()
        self.insertTab =  InsertPdfWindow()


        self.setGeometry(200, 200, 500,300)
        self.scrollArea =QScrollArea()
        webLink="<a href=\"https://github.com/sabar183ahuja/Pdf-Edit-and-Merge/tree/master/\"> Instructions </a>"
        self.webInfo =QLabel(self)
        self.webInfo.setText(webLink)
        self.webInfo.setOpenExternalLinks(True)
        self.statusBar().addWidget(self.webInfo)
        #set as permanent widget to position on bottom right corner
        self.lbl = QLabel("sabar.singh183@gmail.com",self)
        self.statusBar().addPermanentWidget(self.lbl)
        self.statusBar().setStyleSheet("QStatusBar{border-top: 2px outset grey;}")

        self.startUpdateWindow()


    def startUpdateWindow(self):
        self.updateTab.initUI(self)
        self.updateTab.MergeWindowButton.clicked.connect(self.startMergeWindow)
        self.updateTab.deleteWindowButton.clicked.connect(self.startDeleteWindow)
        self.updateTab.InsertWindowButton.clicked.connect(self.startInsertWindow)
        self.show()

    def startMergeWindow(self):
        self.mergeTab.initUI(self)
        self.mergeTab.fileUploaderButton.clicked.connect(self.startUpdateWindow)
        self.mergeTab.deleteWindowButton.clicked.connect(self.startDeleteWindow)
        self.mergeTab.InsertWindowButton.clicked.connect(self.startInsertWindow)
        self.show()

    def startDeleteWindow(self):
        self.deleteTab.initUI(self)
        self.deleteTab.fileUploaderButton.clicked.connect(self.startUpdateWindow)
        self.deleteTab.MergeWindowButton.clicked.connect(self.startMergeWindow)
        self.deleteTab.InsertWindowButton.clicked.connect(self.startInsertWindow)
        self.show()

    def startInsertWindow(self):
        self.insertTab.initUI(self)
        self.insertTab.fileUploaderButton.clicked.connect(self.startUpdateWindow)
        self.insertTab.MergeWindowButton.clicked.connect(self.startMergeWindow)
        self.insertTab.deleteWindowButton.clicked.connect(self.startDeleteWindow)
        self.show()


from mergePdf import MergePdfWindow
from deletePage import DeletePageWindow
from updatePdf import UpdatePdfWindow
from InsertPdf import InsertPdfWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
