# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ApiCompatTest
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from apicompattestdialog import ApiCompatTestDialog

import apicompat

import sip
import unittest
from settings_test import *


class ApiCompatTest:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/apicompattest"
        # Create the dialog (after translation) and keep reference
        self.dlg = ApiCompatTestDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/apicompattest/icon.png"),
            u"Test apicompat", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&apicompattest", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&apicompattest", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        # show the dialog
        self.dlg.show()

        text = self.dlg.ui.text
        text.append("QGIS " + QGis.QGIS_VERSION)
        text.append("SIP " + sip.SIP_VERSION_STR + " API V" + str(sip.getapi("QVariant")))
        text.append("\n")
        suite = unittest.TestLoader().loadTestsFromTestCase(TestSettings)
        unittest.TextTestRunner(verbosity=2, stream=self.dlg).run(suite)

        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            pass