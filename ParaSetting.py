import sys
import os.path
from PyQt5.QtCore import pyqtSlot,QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget,QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QAction, QFileDialog)

global config # the darknet.exe folder
global imageLstName #image list file name
 
class ParaSetting(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 531)
        
        self.Application = QtWidgets.QLabel(Form)
        self.Application.setGeometry(QtCore.QRect(20, 50, 50, 12))
        self.Application.setObjectName("Application")
        
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 300))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # select darknet.exe folder               
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 20, 100, 12))
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 20, 200, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # select image lists file             
        self.labelLst = QtWidgets.QLabel(self.frame)
        self.labelLst.setGeometry(QtCore.QRect(10, 60, 80, 12))
        self.labelLst.setObjectName("labelLst")
        
        self.Editlst = QtWidgets.QLineEdit(self.frame)
        self.Editlst.setGeometry(QtCore.QRect(90, 60, 200, 20))
        self.Editlst.setObjectName("Editlst")
        
        self.pushButtonLst = QtWidgets.QPushButton(self.frame)
        self.pushButtonLst.setGeometry(QtCore.QRect(300, 60, 100, 23))
        self.pushButtonLst.setObjectName("pushButtonLst")
        
        # confirm button
        self.OkButton = QtWidgets.QPushButton(self.frame)
        self.OkButton.setGeometry(QtCore.QRect(200, 150, 75, 23))
        self.OkButton.setObjectName("OkButton")
        
        self.retranslateUi(Form)
        
        self.pushButton.clicked.connect(self.openDirDialog)
        self.pushButtonLst.clicked.connect(self.browseSlot)

        self.OkButton.clicked.connect(self.close)
       
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # select darknet.exe folder 
        MainWindow.setWindowTitle(_translate("MainWindow", "para setting"))
        self.label.setText(_translate("MainWindow", "Darknet Folder"))
        self.pushButton.setText(_translate("MainWindow", "select dir"))

        # select image lists file 
        self.labelLst.setText(_translate("MainWindow", "image lists file"))
        self.pushButtonLst.setText(_translate("MainWindow", "select file"))

        # confirm button
        self.OkButton.setText(_translate("MainWindow", "OK"))

    def browseSlot( self ):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        if fileName:
            print(fileName)
            self.Editlst.setText(fileName)
            global imageLstName
            imageLstName = fileName

    def openDirDialog( self ):
        # 実行ディレクトリ取得
        rootpath = os.path.abspath(os.path.dirname("__file__"))
        # ディレクトリ選択ダイアログを表示
        path = QFileDialog.getExistingDirectory(None, "rootpath", rootpath)
        self.lineEdit.setText(path)
        global config 
        config = self.lineEdit.text()
