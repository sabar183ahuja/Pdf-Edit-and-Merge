"""
    Author: Sabar Singh Ahuja
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from os.path import expanduser
import PyPDF2
import Helper


class UpdatePdfWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Pdf Update page"
        self.pdfToUpdate =''
        self.pdfWithUpdatedPage = ''

    def initUI(self,MainWindow):

        MainWindow.setWindowTitle(self.title)
        self.centralwidget = QWidget(MainWindow)

        firstFileLabel = QLabel('Pdf to Edit:',self.centralwidget)
        firstFileLabel.setGeometry(10,50,70,30)

        browsePdfToUpdateButton = QPushButton('Browse', self.centralwidget)
        browsePdfToUpdateButton.setToolTip('Browse first pdf file')
        browsePdfToUpdateButton.move(300,50)
        browsePdfToUpdateButton.clicked.connect(self.browsePdfToUpdate)
        #self.disp.setStyleSheet('background-color: white')
        self.firstFilePath = QLabel('',self.centralwidget)
        self.firstFilePath.setGeometry(90,50,200,30)
        self.firstFilePath.setStyleSheet('background-color: white')

        secondFileLabel = QLabel('Page to Update:',self.centralwidget)
        secondFileLabel.setGeometry(10,90,90,30)

        self.pageToUpdate = QLineEdit(self.centralwidget)
        self.pageToUpdate.setGeometry(110,90,50,30)
        self.pageToUpdate.setStyleSheet('background-color: white')

        mergedFileLocLabel = QLabel('Pdf with Updated Page:',self.centralwidget)
        mergedFileLocLabel.setGeometry(5,130,130,30)

        browseDestinatonButton = QPushButton('Browse', self.centralwidget)
        # browseDestinatonButton.setToolTip('Browse first pdf file')
        browseDestinatonButton.move(350,130)
        browseDestinatonButton.clicked.connect(self.browsePdfWithUpdatedPage)

        self.newFilePath = QLabel('',self.centralwidget)
        self.newFilePath.setGeometry(140,130,200,30)
        self.newFilePath.setStyleSheet('background-color: white')

        newFileNameLabel=QLabel('Page number of updated page:',self.centralwidget)
        newFileNameLabel.setGeometry(10,170,185,30)

        self.updatedPage = QLineEdit(self.centralwidget)
        self.updatedPage.move(195,175)
        self.updatedPage.setStyleSheet('background-color: white')
        self.updatedPage.resize(50,25)

        updateButton= QPushButton('Update!', self.centralwidget)
        updateButton.setGeometry(150,210,150,30)
        updateButton.setToolTip( "Merge chosen pdf\'s")
        updateButton.clicked.connect(self.updatePdf)
        # page buttons ui
        updatePageButton = QPushButton('Update a page',self.centralwidget)
        updatePageButton.setGeometry(0,0,90,30)
        updatePageButton.setFlat(True)

        self.MergeWindowButton = QPushButton('Merge Pdf', self.centralwidget)
        self.MergeWindowButton.setGeometry(90,0,150,30)
        self.MergeWindowButton.setToolTip( 'convert')

        self.deleteWindowButton = QPushButton('Delete a Page', self.centralwidget)
        self.deleteWindowButton.setGeometry(240,00,100,30)

        self.InsertWindowButton = QPushButton('Insert Page', self.centralwidget)
        self.InsertWindowButton.setGeometry(340,00,100,30)


       	MainWindow.setCentralWidget(self.centralwidget)
    def updatePdf(self):
        try:
            originalPDF = PyPDF2.PdfFileReader(self.pdfToUpdate)
            updatedPagePDF = PyPDF2.PdfFileReader(self.pdfWithUpdatedPage)
        except:
            Helper.DialogBox("Error in opening file")
            return
        try:
            pageToUpdate = int(self.pageToUpdate.text())
            updatedPage = int(self.updatedPage.text())
        except:
            Helper.DialogBox("Enter valid integar!")
            return

        updatedPDF = PyPDF2.PdfFileWriter()
        updatedPDF.cloneDocumentFromReader(originalPDF)
        try:
            updatedPDF.insertPage(updatedPagePDF.getPage(updatedPage - 1), pageToUpdate - 1)
        except IndexError:
            Helper.DialogBox('Index Error!')
            return

        outputFile = open(self.pdfToUpdate, 'wb')

        pdfOut = PyPDF2.PdfFileWriter()

        for i in range(updatedPDF.getNumPages()):
            if i != pageToUpdate:
                pdfOut.addPage(updatedPDF.getPage(i))

        pdfOut.write(outputFile)
        outputFile.close()
        Helper.DialogBox("Pdf Updated!")

    def browsePdfToUpdate(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.pdfToUpdate = FileLoc
        self.firstFilePath.setText(FileLoc)

    def browsePdfWithUpdatedPage(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.pdfWithUpdatedPage = FileLoc
        self.newFilePath.setText(FileLoc)
