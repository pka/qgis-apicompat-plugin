# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ApiCompatTestDialog
                                 A QGIS plugin
 Test suite for apicompat
                             -------------------
        begin                : 2013-07-02
        copyright            : (C) 2013 by Pirmin Kalberer, Sourcepole
        email                : pka@sourcepole.ch
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_apicompattest import Ui_ApiCompatTest
# create the dialog for zoom to point


class ApiCompatTestDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_ApiCompatTest()
        self.ui.setupUi(self)

    def write(self, m):
        self.ui.text.append( m )

    def flush(self):
        pass
