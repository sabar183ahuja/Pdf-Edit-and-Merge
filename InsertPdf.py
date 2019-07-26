"""
    Author: Sabar Singh Ahuja
"""

from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import PyPDF2
import Helper
#developed libraries

class InsertPdfWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Pdf Insert Page"
        self.pdf2update =''
        self.pdf2insert = ''

    def initUI(self,MainWindow):

        MainWindow.setWindowTitle(self.title)
        self.centralwidget = QWidget(MainWindow)

        pdf2UpdateLabel = QLabel('Pdf to Update:',self.centralwidget)
        pdf2UpdateLabel.setGeometry(10,50,70,30)

        browsepdf2UpdateButton = QPushButton('Browse', self.centralwidget)
        browsepdf2UpdateButton.setToolTip('Browse first pdf file')
        browsepdf2UpdateButton.move(300,50)
        browsepdf2UpdateButton.clicked.connect(self.browsePdf2Update)
        #self.disp.setStyleSheet('background-color: white')

        self.pdf2UpdatePath = QLabel('',self.centralwidget)
        self.pdf2UpdatePath.setGeometry(90,50,200,30)
        self.pdf2UpdatePath.setStyleSheet('background-color: white')

        secondFileLabel = QLabel('Page no to insert new page:',self.centralwidget)
        secondFileLabel.setGeometry(10,90,180,30)

        self.pageToInsert =  QLineEdit(self.centralwidget)
        self.pageToInsert.setGeometry(180,90,50,30)
        self.pageToInsert.setStyleSheet('background-color: white')

        pdf2insertLabel = QLabel('Pdf to be inserted:',self.centralwidget)
        pdf2insertLabel.setGeometry(5,130,140,30)

        browseDestinatonButton = QPushButton('Browse', self.centralwidget)
        # browseDestinatonButton.setToolTip('Browse first pdf file')
        browseDestinatonButton.move(330,130)
        browseDestinatonButton.clicked.connect(self.browsePdf2Insert)

        self.pdf2insertPath= QLabel('',self.centralwidget)
        self.pdf2insertPath.setGeometry(120,130,200,30)
        self.pdf2insertPath.setStyleSheet('background-color: white')


        updateButton= QPushButton('Update!', self.centralwidget)
        updateButton.setGeometry(150,210,150,30)
        updateButton.setToolTip( "Update pdf")
        updateButton.clicked.connect(self.updatePdf)

        # page buttons ui
        self.fileUploaderButton = QPushButton('Update a Page',self.centralwidget)
        self.fileUploaderButton.setGeometry(0,0,90,30)

        self.MergeWindowButton= QPushButton('Merge Pdf', self.centralwidget)
        self.MergeWindowButton.setGeometry(90,0,150,30)
        self.MergeWindowButton.setToolTip( 'convert')

        self.deleteWindowButton = QPushButton('Delete a Page', self.centralwidget)
        self.deleteWindowButton.setGeometry(240,00,100,30)

        InsertWindowButton = QPushButton('Insert Page', self.centralwidget)
        InsertWindowButton.setGeometry(340,00,100,30)
        InsertWindowButton.setFlat(True)


        MainWindow.setCentralWidget(self.centralwidget)
    def updatePdf(self):
        try:
            originalPDF = PyPDF2.PdfFileReader(self.pdf2update)
            PDFwithInsert = PyPDF2.PdfFileReader(self.pdf2insert)
        except:
            Helper.DialogBox("Error in opening files")
            return
        updatedPDF = PyPDF2.PdfFileWriter()
        updatedPDF.cloneDocumentFromReader(originalPDF)
        try:
            pageWithInsert=int(self.pageToInsert.text())
        except:
            Helper.DialogBox("Please enter an integar!")
            return

        try:
            for i in range( PDFwithInsert.getNumPages()):
                updatedPDF.insertPage(PDFwithInsert.getPage(i), pageWithInsert - 1+i)
        except IndexError:
            Helper.DialogBox(" IndexError!")
            return

        outputFile = open(self.pdf2update, 'wb')
        pdfOut = PyPDF2.PdfFileWriter()

        for i in range(updatedPDF.getNumPages()):
            pdfOut.addPage(updatedPDF.getPage(i))

        pdfOut.write(outputFile)
        outputFile.close()
        Helper.DialogBox("Page Inserted!!")

    def browsePdf2Update(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.pdf2update = FileLoc
        self.pdf2UpdatePath.setText(FileLoc)

    def browsePdf2Insert(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.pdf2insert= FileLoc
        self.pdf2insertPath.setText(FileLoc)
