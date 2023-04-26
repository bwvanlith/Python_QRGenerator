
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import *
from PIL.ImageQt import ImageQt
import qrcode
import sys

img = qrcode.make(data=None)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        global img
        Dialog.setObjectName("Dialog")
        Dialog.resize(384, 546)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushGenerate = QtWidgets.QPushButton(Dialog)
        self.pushGenerate.setGeometry(QtCore.QRect(70, 140, 110, 23))
        self.pushGenerate.setObjectName("pushGenerate")

        qimage = ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.label_qr = QtWidgets.QLabel(Dialog)
        self.label_qr.setPixmap(pixmap)
        self.label_qr.move(50, 175)

        self.pushSave = QtWidgets.QPushButton(Dialog)
        self.pushSave.setGeometry(QtCore.QRect(70, 470, 110, 23))
        self.pushSave.setObjectName("pushSave")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 110, 251, 20))
        self.lineEdit.setInputMask("")
        self.lineEdit.setObjectName("lineEdit")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(70, 490, 251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(70, 90, 251, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 70, 251, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 40, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QR Image Generator"))
        self.pushGenerate.setText(_translate("Dialog", "Generate QR Image"))
        self.pushGenerate.clicked.connect(self.generateQR)
        self.pushSave.setText(_translate("Dialog", "Save QR Image"))
        self.pushSave.clicked.connect(self.saveQR)
        self.lineEdit.setText(_translate("Dialog", "Enter your url here..."))
        self.label.setText(_translate("Dialog", "Enter an url and click the generate button"))
        self.label_2.setText(_translate("Dialog", "QR Image Generator"))

    def generateQR(self):
        global img
        global QRImage
        input = self.lineEdit.text()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
        )
        qr.add_data(input)
        qr.make(fit=True)
        img = qr.make_image(fill="black", backcolor="white")

        qimage = ImageQt(img)
        pixmap = QtGui.QPixmap.fromImage(qimage)
        self.label_qr.setPixmap(pixmap)





    def saveQR(self):
        global img
        url = self.lineEdit.text()
        suffix = '.png'
        filename = 'QR'
        img.save(f'{filename}_{url}{suffix}')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
