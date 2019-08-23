#standard libraries
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyPDF2
import Helper



class MergePdfWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = "Pdf Merge Pdf\'s"
        self.firstFile=''
        self.secondFile =''
        self.mergedPdfName=''
        self.mergedFilePath =''

    def initUI(self,MainWindow):
        MainWindow.setWindowTitle(self.title)
        self.centralwidget = QWidget(MainWindow)

        ### butttons ui
        firstFileLabel = QLabel('First File:',self.centralwidget)
        firstFileLabel.setGeometry(10,50,70,30)

        browseFirstFileButton = QPushButton('Browse', self.centralwidget)
        browseFirstFileButton.setToolTip('Browse first pdf file')
        browseFirstFileButton.move(300,50)
        browseFirstFileButton.clicked.connect(self.browseFirstFile)
        #self.disp.setStyleSheet('background-color: white')
        self.firstFilePath = QLabel('',self.centralwidget)
        self.firstFilePath.setGeometry(90,50,200,30)
        self.firstFilePath.setStyleSheet('background-color: white')

        secondFileLabel = QLabel('Second File:',self.centralwidget)
        secondFileLabel.setGeometry(10,90,70,30)

        browsesecondFileButton = QPushButton('Browse', self.centralwidget)
        browsesecondFileButton.setToolTip('Browse second pdf file')
        browsesecondFileButton.move(300,90)
        browsesecondFileButton.clicked.connect(self.browseSecondFile)

        self.secondFilePath = QLabel('',self.centralwidget)
        self.secondFilePath.setGeometry(90,90,200,30)
        self.secondFilePath.setStyleSheet('background-color: white')

        mergedFileLocLabel = QLabel('New File location:',self.centralwidget)
        mergedFileLocLabel.setGeometry(5,130,105,30)

        browseDestinatonButton = QPushButton('Browse', self.centralwidget)
        # browseDestinatonButton.setToolTip('Browse first pdf file')
        browseDestinatonButton.move(330,130)
        browseDestinatonButton.clicked.connect(self.browseNewFileFolder)

        self.newFilePath = QLabel('',self.centralwidget)
        self.newFilePath.setGeometry(120,130,200,30)
        self.newFilePath.setStyleSheet('background-color: white')

        newFileNameLabel=QLabel('New File Name:',self.centralwidget)
        newFileNameLabel.setGeometry(10,170,90,30)

        self.newFileNametext = QLineEdit(self.centralwidget)
        self.newFileNametext.move(110,170)
        self.newFileNametext.setStyleSheet('background-color: white')
        self.newFileNametext.resize(90,25)

        mergeButton= QPushButton('Merge!', self.centralwidget)
        mergeButton.setGeometry(150,210,150,30)
        mergeButton.setToolTip( "Merge chosen pdf\'s")
        mergeButton.clicked.connect(self.mergePdf)
        #  page buttpsm ui
        MergeWindowButton = QPushButton('Merge Pdf', self.centralwidget)
        MergeWindowButton.setGeometry(90,00,150,30)
        MergeWindowButton.setFlat(True)


        self.fileUploaderButton = QPushButton('Update a Page',self.centralwidget)
        self.fileUploaderButton.setGeometry(0,00,90,30)

        self.deleteWindowButton = QPushButton('Delete a Page', self.centralwidget)
        self.deleteWindowButton.setGeometry(240,00,100,30)

        self.InsertWindowButton = QPushButton('Insert Page', self.centralwidget)
        self.InsertWindowButton.setGeometry(340,00,100,30)

       	MainWindow.setCentralWidget(self.centralwidget)
# as

    def mergePdf(self):
        mergedPdf= PyPDF2.PdfFileMerger()
        try:
            mergedPdf.append(self.firstFile)
            mergedPdf.append(self.secondFile)
        except:
            Helper.DialogBox("Error in opening files")
            return
         
        fullbook = open(self.mergedFilePath+"/"+self.newFileNametext.text() + '.pdf', 'wb')
        mergedPdf.write(fullbook)
        mergedPdf.close()
        Helper.DialogBox("Pdf's Merged!!")
        # adf pop up winodw

    def browseFirstFile(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.firstFile = FileLoc
        self.firstFilePath.setText(FileLoc)

    def browseSecondFile(self):
        options = QFileDialog.Options()
        FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
        self.secondFile = FileLoc
        self.secondFilePath.setText(FileLoc)

    def browseNewFileFolder(self):
        self.mergedFilePath = QFileDialog.getExistingDirectory(None, 'Select a folder:', expanduser("~"))
        self.newFilePath.setText(self.mergedFilePath)
