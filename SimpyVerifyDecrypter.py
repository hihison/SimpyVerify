# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import requests
import json
import cryptocode
import pyperclip

key = "<Put Key Here>"
crypted = "Nothing Yet"
version = 1.2
class Ui_Dialog(object):
    
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(400, 300)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(300, 240, 71, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setMinimumSize(QSize(0, 0))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 371, 231))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)

        """
        self.label_IP = QLabel(self.formLayoutWidget)
        self.label_IP.setObjectName(u"label_IP")"""

        #self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_IP)
        """
        self.textEdit_IP = QTextEdit(self.formLayoutWidget)
        self.textEdit_IP.setObjectName(u"textEdit_IP")
        self.textEdit_IP.setMaximumSize(QSize(16777215, 30))
        self.textEdit_IP.setReadOnly(True)
        self.textEdit_IP.setAcceptRichText(False)"""
        #ip = get_ip(1)
        #self.textEdit_IP.setHtml()

        #self.formLayout.setWidget(0, QFormLayout.FieldRole, self.textEdit_IP)

        self.label_connection = QLabel(self.formLayoutWidget)
        self.label_connection.setObjectName(u"label_connection")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_connection)

        self.textEdit_connection = QTextEdit(self.formLayoutWidget)
        self.textEdit_connection.setObjectName(u"textEdit_connection")
        self.textEdit_connection.setMaximumSize(QSize(16777215, 90))
        self.textEdit_connection.setReadOnly(False)
        self.textEdit_connection.setAcceptRichText(False)
        #ipdata = get_ip(2)
        #rawdata = json.dumps({'IP':ip,'Organization': ipdata[0], 'ISP': ipdata[1], 'Region':ipdata[3]}, separators=(',', ': '))
        global crypted
        #crypted = encrypter(rawdata,key)
        #self.textEdit_connection.setHtml("Organization : "+ipdata[0]+"<br>ISP : "+ipdata[1]+"<br>Region : "+ipdata[3])
        #self.textEdit_connection.setHtml(crypted)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.textEdit_connection)

        self.pushButton_copy = QPushButton(Dialog)
        self.pushButton_copy.setObjectName(u"pushButton_copy")
        self.pushButton_copy.setGeometry(QRect(20, 220, 261, 61))
        #self.pushButton_copy.setCheckable(True)
        #self.pushButton_copy.toggle()
        self.pushButton_copy.clicked.connect(lambda:self.whichbtn(self.pushButton_copy))
        self.pushButton_copy.clicked.connect(self.btnstate())

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-4, 19, 401, 41))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.labelV = QLabel(Dialog)
        self.labelV.setObjectName(u"labelV")
        self.labelV.setGeometry(QRect(340, 30, 401, 41))
        fontV = QFont()
        fontV.setPointSize(18)
        fontV.setBold(False)
        fontV.setWeight(30)
        self.labelV.setStyleSheet("color: #FF8800;font-weight: bold;");
        self.labelV.setFont(fontV)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)



        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"SimpyVerify Decrypter", None))
        #self.label_IP.setText(QCoreApplication.translate("Dialog", u"IP address", None))
        self.label_connection.setText(QCoreApplication.translate("Dialog", u"Secret Magic Key", None))
        self.pushButton_copy.setText(QCoreApplication.translate("Dialog", u"Decrypt", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"SimpyVerify Decrypter", None))
        self.labelV.setText(QCoreApplication.translate("Dialog", str(version), None))

    # retranslateUi


    def whichbtn(self,b):
        print ("clicked button is "+b.text())
        if b.text()=="Decrypt":
            global crypted
            try:
                crypted = self.textEdit_connection.toPlainText()
                decrypted = decrypter(crypted,key)
                decrypted = json.loads(decrypted)
            
                outmsg = "IP: "+decrypted["IP"]+"<br>Organization: "+decrypted["Organization"]+"<br>ISP: "+decrypted["ISP"]+"<br>Region: "+decrypted["Region"]+"<br>HWID: "+decrypted["HWID"]
            except:
                outmsg = "Invalid data"
            #pyperclip.copy(crypted)
            #self.pushButton_copy.setText(QCoreApplication.translate("Dialog", u"Copied", None))
            msg = QMessageBox()
            msg.setWindowTitle("Alert")
            msg.setText(outmsg)
            msg.setIcon(QMessageBox.Information)
            #x = msg.exec_()
            self.textEdit_connection.setHtml(outmsg)

    def btnstate(self):
        if self.pushButton_copy.isChecked():
            print ("button clicked")
            

        else:
            print ("button released")

            



def get_ip(mode):
    try:
        rdata = requests.get('http://ipwho.is/').text
    except requests.exceptions.Timeout:
        return "err01"
        # Maybe set up for a retry, or continue in a retry loop
    except requests.exceptions.TooManyRedirects:
        return "err02"
        # Tell the user their URL was bad and try a different one
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        return "err03"
        #raise SystemExit(e)

    data = json.loads(rdata)
    if mode==1:
        return data["ip"]
    if mode==2:
        return data["connection"]["org"],data["connection"]["isp"],data["connection"]["isp"],data["region"]
    
def encrypter(data,key_e):
    str_encoded = cryptocode.encrypt(data,key_e)
    return str_encoded

def decrypter(data,key_e):
    str_decoded = cryptocode.decrypt(data,key_e) 
    return str_decoded


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())