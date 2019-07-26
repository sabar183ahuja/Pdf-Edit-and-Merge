"""
    Author: Sabar Singh Ahuja
"""
import PyPDF2
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import Helper

class DeletePageWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.title = 'Pdf Delete a Page'
		self.pdf2update = ''

	"""
	initalizes ui for logo generator and connects it's events to functions
	"""
	def initUI(self,MainWindow):
		MainWindow.setWindowTitle(self.title)
		self.centralwidget = QWidget(MainWindow)

		pdf2UpdateLabel = QLabel('Pdf to Update:',self.centralwidget)
		pdf2UpdateLabel.setGeometry(10,50,70,30)

		browsepdf2UpdateButton = QPushButton('Browse', self.centralwidget)
		browsepdf2UpdateButton.setToolTip('Browse first pdf file')
		browsepdf2UpdateButton.move(300,50)
		browsepdf2UpdateButton.clicked.connect(self.browsePdf2Update)

		self.pdf2UpdatePath = QLabel('',self.centralwidget)
		self.pdf2UpdatePath.setGeometry(90,50,200,30)
		self.pdf2UpdatePath.setStyleSheet('background-color: white')

		deletePageLabel = QLabel('Page number to Delete:',self.centralwidget)
		deletePageLabel.setGeometry(10,90,180,30)

		self.pageToDeleteInput =  QLineEdit(self.centralwidget)
		self.pageToDeleteInput.setGeometry(160,90,50,30)
		self.pageToDeleteInput.setStyleSheet('background-color: white')

		deleteButton= QPushButton('Delete!', self.centralwidget)
		deleteButton.setGeometry(150,210,150,30)
		deleteButton.setToolTip( "Update pdf")
		deleteButton.clicked.connect(self.updatePdf)
		# Page buttons ui
		self.fileUploaderButton = QPushButton('Update a Page',self.centralwidget)
		self.fileUploaderButton.setGeometry(0,0,90,30)

		self.MergeWindowButton = QPushButton('Merge pdf', self.centralwidget)
		self.MergeWindowButton.setGeometry(90,0,150,30)
		self.MergeWindowButton.setToolTip( 'convert')

		self.InsertWindowButton = QPushButton('Insert a Page', self.centralwidget)
		self.InsertWindowButton.setGeometry(340,00,100,30)

		deleteWindowButton = QPushButton('Delete a Page', self.centralwidget)
		deleteWindowButton.setGeometry(240,0,100,30)
		deleteWindowButton.setFlat(True)

		MainWindow.setCentralWidget(self.centralwidget)

	def updatePdf(self):
		try:
			originalPDF = PyPDF2.PdfFileReader(self.pdf2update)
			updatedPDF = PyPDF2.PdfFileWriter()
		except:
			Helper.DialogBox("Error in Opening files")
			return
		updatedPDF.cloneDocumentFromReader(originalPDF)

		try:
			pageToDelete=int(self.pageToDeleteInput.text())
		except:
			Helper.DialogBox("Please enter an integar")
			return

		if pageToDelete <= 0 or pageToDelete > originalPDF.getNumPages()-1:
			Helper.DialogBox("Index Error")
			return

		outputFile = open(self.pdf2update, 'wb')
		pdfOut = PyPDF2.PdfFileWriter()

		for i in range(updatedPDF.getNumPages()):
			if i != pageToDelete - 1:
				pdfOut.addPage(updatedPDF.getPage(i))

		pdfOut.write(outputFile)
		outputFile.close()
		Helper.DialogBox("Page Deleted!")

	def browsePdf2Update(self):
		options = QFileDialog.Options()
		FileLoc, _ = QFileDialog.getOpenFileName(self,"Select File",expanduser("~"),"(*.pdf)", options=options)
		self.pdf2update = FileLoc
		self.pdf2UpdatePath.setText(FileLoc)
