# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_apicompattest.ui'
#
# Created: Wed Jul  3 00:26:30 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ApiCompatTest(object):
    def setupUi(self, ApiCompatTest):
        ApiCompatTest.setObjectName(_fromUtf8("ApiCompatTest"))
        ApiCompatTest.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(ApiCompatTest)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.text = QtGui.QTextEdit(ApiCompatTest)
        self.text.setUndoRedoEnabled(False)
        self.text.setReadOnly(True)
        self.text.setHtml(_fromUtf8("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.text.setAcceptRichText(False)
        self.text.setObjectName(_fromUtf8("text"))
        self.verticalLayout.addWidget(self.text)
        self.buttonBox = QtGui.QDialogButtonBox(ApiCompatTest)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ApiCompatTest)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ApiCompatTest.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ApiCompatTest.reject)
        QtCore.QMetaObject.connectSlotsByName(ApiCompatTest)

    def retranslateUi(self, ApiCompatTest):
        ApiCompatTest.setWindowTitle(QtGui.QApplication.translate("ApiCompatTest", "ApiCompatTest", None, QtGui.QApplication.UnicodeUTF8))

