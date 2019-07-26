"""
    Author: Sabar Singh Ahuja
"""
from PyQt5.QtWidgets import *
from os.path import expanduser
import PyPDF2

def DialogBox(str):
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)
   msg.setWindowTitle('PDF')
   msg.setText(str)

   retval = msg.exec_()
