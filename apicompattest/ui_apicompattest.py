# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_apicompattest.ui'
#
# Created: Tue Jul  2 21:10:02 2013
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
        self.buttonBox = QtGui.QDialogButtonBox(ApiCompatTest)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(ApiCompatTest)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ApiCompatTest.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ApiCompatTest.reject)
        QtCore.QMetaObject.connectSlotsByName(ApiCompatTest)

    def retranslateUi(self, ApiCompatTest):
        ApiCompatTest.setWindowTitle(QtGui.QApplication.translate("ApiCompatTest", "ApiCompatTest", None, QtGui.QApplication.UnicodeUTF8))

